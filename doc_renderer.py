# doc_renderer.py

import os
from jinja2 import Environment, FileSystemLoader, select_autoescape
from typing import Dict, List


def render_docs(definitions: List[Dict], llm_responses: Dict[str, str],
                output_dir: str = "docs", template_dir: str = "templates"):
    """
    Генерирует Markdown-документацию по списку определений и ответам LLM.

    :param definitions: список словарей с полями:
        - "file": путь к файлу
        - "type": тип определения (function, class, method)
        - "name": имя определения
        - "line": строка в исходнике
    :param llm_responses: dict, ключ = уникальный id определения (file:name:line),
                          значение = текст описания от LLM
    :param output_dir: папка для вывода Markdown-файлов
    :param template_dir: папка с шаблонами Jinja2
    """
    # Настройка окружения Jinja2
    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=select_autoescape()
    )
    template = env.get_template('doc_template.md.j2')

    # Убедимся, что папка есть
    os.makedirs(output_dir, exist_ok=True)

    for d in definitions:
        key = f"{d['file']}:{d['name']}:{d['line']}"
        description = llm_responses.get(key, '_Описание не сгенерировано_')

        # Если нет snippet, подгружаем из файла: 2 строки до и 2 после
        snippet = d.get('snippet')
        if not snippet:
            try:
                with open(d['file'], encoding='utf-8') as src:
                    lines = src.readlines()
                center = d['line'] - 1
                start = max(0, center - 2)
                end = min(len(lines), center + 3)
                snippet = ''.join(lines[start:end]).rstrip()
            except Exception:
                snippet = ''

        # Рендерим шаблон
        rendered = template.render(
            file=d['file'],
            type=d['type'],
            name=d['name'],
            line=d['line'],
            snippet=snippet,
            description=description
        )

        # Формируем имя выходного файла
        fname = f"{os.path.splitext(os.path.basename(d['file']))[0]}_{d['type']}_{d['name']}_line{d['line']}.md"
        out_path = os.path.join(output_dir, fname)
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(rendered)
