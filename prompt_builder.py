# prompt_builder.py

import os
from typing import List, Dict

def extract_snippet(path: str, lineno: int, context: int = 3) -> str:
    """
    Возвращает контекст вокруг строки lineno (3 строки до и после по умолчанию).
    """
    with open(path, encoding='utf-8') as f:
        lines = f.read().splitlines()
    start = max(0, lineno - 1 - context)
    end   = min(len(lines), lineno - 1 + context + 1)
    # нумеруем строки внутри сниппета относительной строкой определения
    snippet_lines = []
    for idx in range(start, end):
        prefix = ">" if idx == lineno - 1 else " "
        snippet_lines.append(f"{prefix} {idx+1:4d}: {lines[idx]}")
    return "\n".join(snippet_lines)

def build_prompts(
    definitions: List[Dict[str, any]],
    repo_root: str
) -> Dict[str, str]:
    """
    Для каждого определения собирает ключ и текст промпта.
    Ключ — "<файл>:<имя>:<строка>"
    Промпт включает сниппет и инструкцию "Опиши, как это работает".
    """
    prompts: Dict[str, str] = {}
    for defn in definitions:
        kind = defn['type']
        name = defn['name']
        lineno = defn['line']
        relpath = defn['file']
        abspath = os.path.join(repo_root, relpath)

        # Берём код вокруг определения
        snippet = extract_snippet(abspath, lineno)

        # Формируем ключ и промпт
        key = f"{relpath}:{name}:{lineno}"
        lang = os.path.splitext(relpath)[1].lstrip('.')  # py, cpp, js...

        prompt = (
            f"Файл: {relpath}\n"
            f"Тип: {kind}\n"
            f"Имя: {name}\n"
            f"Строка: {lineno}\n\n"
            f"Код ({lang}):\n"
            f"```\n{snippet}\n```\n\n"
            "Пожалуйста, опиши, как этот блок кода работает и для чего он нужен.\n"
        )

        prompts[key] = prompt

    return prompts
