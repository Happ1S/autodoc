import ast
import textwrap
import pytest

from astparserpy.parser import parse_file, extract_definitions, Definition

def make_py_file(tmp_path, filename: str, content: str):
    file_path = tmp_path / filename
    file_path.write_text(textwrap.dedent(content), encoding="utf-8")
    return str(file_path)

def test_parse_file_returns_ast_module(tmp_path):
    code = """
    # простой модуль
    x = 1
    def foo(): pass
    """
    path = make_py_file(tmp_path, "mod1.py", code)
    mod = parse_file(path)
    assert isinstance(mod, ast.Module)
    names = [n.name for n in mod.body if isinstance(n, ast.FunctionDef)]
    assert "foo" in names

def test_extract_definitions_empty(tmp_path):
    code = """
    # файл без функций и классов
    a = 10
    b = a + 5
    """
    path = make_py_file(tmp_path, "empty.py", code)
    defs = extract_definitions(parse_file(path))
    assert defs == []

# … остальные тесты без изменений …
