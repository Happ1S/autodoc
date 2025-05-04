#!/usr/bin/env python3
import os
import argparse

from astparserpy.parser import parse_file as parse_py, extract_definitions as extract_py_defs
from astparsercxx.parser import parse_file as parse_cpp, extract_definitions as extract_cpp_defs
from prompt_builder import build_prompts
from llm_client import LLMClient
from doc_renderer import render_docs

def collect_definitions(repo_root: str = '.') -> list[dict]:
    """
    Обходит все файлы в репо и собирает определения:
    - .py → Python AST
    - .cpp/.cc/.h/.hpp → C++ AST
    """
    definitions: list[dict] = []
    for root, _, files in os.walk(repo_root):
        for fn in files:
            path = os.path.join(root, fn)
            rel = os.path.relpath(path, repo_root)
            try:
                if fn.endswith('.py'):
                    tree = parse_py(path)
                    defs = extract_py_defs(tree)
                elif fn.endswith(('.cpp', '.cc', '.h', '.hpp')):
                    tu = parse_cpp(path)
                    defs = extract_cpp_defs(tu)
                else:
                    continue
            except Exception as e:
                print(f"⚠️  Ошибка при парсинге {rel}: {e}")
                continue

            for kind, name, line in defs:
                definitions.append({
                    'file': rel,
                    'type': kind,
                    'name': name,
                    'line': line
                })
    return definitions

def main():
    parser = argparse.ArgumentParser(description="Генератор документации")
    parser.add_argument(
        '--repo-root', '-r',
        default='.',
        help='Путь к корню репозитория, в котором нужно собрать документацию'
    )
    parser.add_argument(
        '--out', '-o',
        default='docs',
        help='Папка для вывода .md-файлов'
    )
    args = parser.parse_args()

    repo_root = args.repo_root
    output_dir = args.out

    print(f"📂 Берём код из: {repo_root}")
    defs = collect_definitions(repo_root)
    print(f"🔎 Найдено определений: {len(defs)}")

    prompts = build_prompts(defs, repo_root)

    client = LLMClient()
    responses = {}
    for key, prompt in prompts.items():
        print(f"✏️  Запрос LLM для {key}...")
        responses[key] = client.complete(prompt)

    render_docs(
        definitions=defs,
        llm_responses=responses,
        output_dir=output_dir,
        template_dir="templates"
    )
    print(f"✅ Готово! Документация в папке {output_dir}/")

if __name__ == "__main__":
    main()
