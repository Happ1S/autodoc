# cxx_ast_parser.py

import os
from clang import cindex
from typing import List, Tuple

# Указываем путь к libclang; настройте под вашу систему
# Убедитесь, что версия libclang соответствует биндингам (clangdev и python-clang-cindex)
cindex.Config.set_library_file("/usr/lib/llvm-17/lib/libclang-17.so.1")
# Отключаем строгую проверку символов
cindex.Config.compatibility_check = False

# Definition = (тип, имя, номер строки)
Definition = Tuple[str, str, int]


def parse_file(path: str, clang_args: List[str] = None) -> cindex.TranslationUnit:
    """
    Парсит C++-файл и возвращает TranslationUnit.
    """
    if clang_args is None:
        clang_args = ['-std=c++17', '-I.']
    index = cindex.Index.create()
    tu = index.parse(path, args=clang_args)
    return tu


def extract_definitions(tu: cindex.TranslationUnit) -> List[Definition]:
    """
    Обходит AST и возвращает список определений:
    - free-functions  -> ("function", имя, строка)
    - classes/structs -> ("class", имя, строка)
    - методы          -> ("method", "ClassName::method", строка)
    """
    defs: List[Definition] = []
    source_file = os.path.abspath(tu.spelling)

    def visitor(cursor):
        for child in cursor.get_children():
            loc = child.location
            # Интересуют только узлы из исходного файла
            if loc.file and os.path.abspath(loc.file.name) == source_file:
                kind = child.kind
                if kind == cindex.CursorKind.FUNCTION_DECL:
                    defs.append(("function", child.spelling, loc.line))
                elif kind in (cindex.CursorKind.CLASS_DECL, cindex.CursorKind.STRUCT_DECL):
                    defs.append(("class", child.spelling, loc.line))
                elif kind == cindex.CursorKind.CXX_METHOD:
                    parent = child.semantic_parent
                    if parent.kind in (cindex.CursorKind.CLASS_DECL, cindex.CursorKind.STRUCT_DECL):
                        defs.append(("method", f"{parent.spelling}::{child.spelling}", loc.line))
            # Рекурсивный обход
            visitor(child)

    visitor(tu.cursor)
    return defs
