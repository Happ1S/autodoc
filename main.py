import os
import ast
import logging
from typing import List, Tuple
from parser import parse_file, extract_definitions
import openai

try:
    from openai.error import (
        AuthenticationError,
        PermissionError as OpenaiPermissionError,
        RateLimitError,
        APIConnectionError,
        OpenAIError,
    )
except ImportError:
    AuthenticationError      = getattr(openai, "AuthenticationError", Exception)
    OpenaiPermissionError    = getattr(openai, "PermissionError", Exception)
    RateLimitError           = getattr(openai, "RateLimitError", Exception)
    APIConnectionError       = getattr(openai, "APIConnectionError", Exception)
    OpenAIError              = getattr(openai, "OpenAIError", Exception)


# ----------------------------
#  Настройка логирования
# ----------------------------
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
fmt = logging.Formatter("%(asctime)s %(levelname)s: %(message)s", "%Y-%m-%d %H:%M:%S")

ch = logging.StreamHandler()
ch.setFormatter(fmt)
logger.addHandler(ch)

fh = logging.FileHandler("generate_docs.log", encoding="utf-8")
fh.setFormatter(fmt)
logger.addHandler(fh)


# ----------------------------
#  Ключ OpenAI из переменных окружения
# ----------------------------
openai.api_key = os.getenv("OPENAI_API_KEY")

Definition = Tuple[str, str, int]


def traverse_repo(root_dir: str) -> List[str]:
    """
    Рекурсивно обходит root_dir и возвращает все .py-файлы.
    """
    py_files = []
    for dirpath, _, filenames in os.walk(root_dir):
        for fn in filenames:
            if fn.endswith(".py"):
                py_files.append(os.path.join(dirpath, fn))
    return py_files


def build_prompt_for_ast(source_ast: ast.Module, definitions: List[Definition]) -> str:
    """
    Собирает в текст prompt: список определений + дамп AST.
    """
    defs_text = "\n".join(f"- {kind} `{name}` (line {lineno})"
                          for kind, name, lineno in definitions)
    ast_dump = ast.dump(source_ast, include_attributes=True, indent=2)
    return (
        "Сгенерируй подробную документацию (docstring или markdown) к этому файлу.\n\n"
        "Список определений:\n"
        f"{defs_text}\n\n"
        "AST-фрагмент модуля:\n"
        f"```python\n{ast_dump}\n```"
    )


def generate_doc_for_file(path: str) -> str:
    """
    Парсит файл, строит prompt и отправляет его в OpenAI.
    При ошибках возвращает текст-плейсхолдер с описанием.
    """
    module      = parse_file(path)
    definitions = extract_definitions(module)
    prompt      = build_prompt_for_ast(module, definitions)

    try:
        resp = openai.chat.completions.create(
            model="gpt-4.1-nano",
            messages=[
                {"role": "system", "content": "Ты — генератор документации по коду."},
                {"role": "user",   "content": prompt}
            ],
            temperature=0.2,
            max_tokens=1500
        )
        content = resp.choices[0].message.content
        return content.strip() if isinstance(content, str) else ""

    except AuthenticationError as e:
        logger.error("Неверный или отсутствующий API-ключ OpenAI: %s", e)
        return "*Ошибка: неверный или отсутствующий API-ключ OpenAI*"

    except OpenaiPermissionError as e:
        logger.error("Доступ запрещён или регион недоступен: %s", e)
        return "*Ошибка: доступ к API запрещён или регион недоступен*"

    except RateLimitError as e:
        logger.error("Превышен лимит запросов к OpenAI: %s", e)
        return "*Ошибка: превышен лимит запросов к OpenAI*"

    except APIConnectionError as e:
        logger.error("Не удалось подключиться к OpenAI API: %s", e)
        return "*Ошибка: не удалось подключиться к OpenAI API*"

    except OpenAIError as e:
        logger.error("Ошибка OpenAI API: %s", e)
        return f"*Ошибка OpenAI API: {e}*"

    except Exception as e:
        logger.exception("Неожиданная ошибка при генерации документации")
        return f"*Неизвестная ошибка: {e}*"


def main(root_dir: str, output_path: str):
    """
    1) Собирает список .py-файлов
    2) Генерирует документацию per-file
    3) Записывает всё в один markdown-файл
    """
    # Если output_path — папка или заканчивается на os.sep, сохраняем docs.md внутри неё
    if output_path.endswith(os.sep) or os.path.isdir(output_path):
        os.makedirs(output_path, exist_ok=True)
        output_file = os.path.join(output_path, "docs.md")
    else:
        output_file = output_path

    logger.info("Начинаем обход репозитория: %s", root_dir)
    py_files = traverse_repo(root_dir)
    if not py_files:
        logger.error("Не найдено ни одного .py-файла в %s. Проверьте путь.", root_dir)
        return

    lines = ["# Автогенерированная документация\n"]
    for path in py_files:
        rel = os.path.relpath(path, root_dir)
        logger.info("Генерируем документацию для %s", rel)
        doc = generate_doc_for_file(path)
        # Гарантируем, что doc — строка
        if not isinstance(doc, str) or not doc.strip():
            doc = "*Ошибка: не удалось сгенерировать документацию для этого файла*"
        lines.append(f"\n## Файл: `{rel}`\n")
        lines.append(doc)

    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        logger.info("Документация успешно сохранена в %s", output_file)
    except Exception as e:
        logger.exception("Не удалось записать файл документации")
        print(f"Ошибка при записи {output_file}: {e}")


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Использование: python main.py <путь_к_репо> <путь_к_выходной_директории_или_файлу>")
        sys.exit(1)
    repo_root, output_md = sys.argv[1], sys.argv[2]
    main(repo_root, output_md)
