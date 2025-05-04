# tests/test_cxx_ast_parser.py

import textwrap
import pytest
from clang import cindex

from astparsercxx.parser import parse_file, extract_definitions, Definition

def make_cpp_file(tmp_path, filename: str, content: str) -> str:
    p = tmp_path / filename
    p.write_text(textwrap.dedent(content), encoding="utf-8")
    return str(p)

def test_parse_file_returns_translation_unit(tmp_path):
    code = """
    // простой free-функция
    int add(int a, int b) {
        return a + b;
    }
    """
    path = make_cpp_file(tmp_path, "add.cpp", code)
    tu = parse_file(path)
    # Должен быть TranslationUnit, и его spelling должен совпадать с путём
    assert isinstance(tu, cindex.TranslationUnit)
    assert tu.spelling.endswith("add.cpp")

def test_extract_definitions_function(tmp_path):
    code = """
    int add(int a, int b) {
        return a + b;
    }
    """
    path = make_cpp_file(tmp_path, "func.cpp", code)
    tu = parse_file(path)
    defs = extract_definitions(tu)
    # Ожидаем ровно одну free-функцию add на строке 2
    assert ("function", "add", 2) in defs
    # Больше ничего
    assert all(d[0] == "function" for d in defs)

def test_extract_definitions_struct_and_method(tmp_path):
    code = """
    struct S {
        int bar(int x) { return x; }
    };
    """
    path = make_cpp_file(tmp_path, "struct.cpp", code)
    tu = parse_file(path)
    defs = extract_definitions(tu)
    # Структура S на строке 2 и метод S::bar на строке 3
    assert ("class", "S", 2) in defs
    assert ("method", "S::bar", 3) in defs

def test_extract_nested_classes(tmp_path):
    code = """
    class Outer {
        class Inner {
            void f() {}
        };
    };
    """
    path = make_cpp_file(tmp_path, "nested.cpp", code)
    tu = parse_file(path)
    defs = extract_definitions(tu)
    # Outer, Inner, и метод Inner::f
    assert ("class", "Outer", 2) in defs
    assert ("class", "Inner", 3) in defs
    assert ("method", "Inner::f", 4) in defs

def test_ignore_includes_and_external(tmp_path):
    code = """
    #include <vector>

    void foo();

    void foo() {
    }
    """
    path = make_cpp_file(tmp_path, "ignore.cpp", code)
    tu = parse_file(path, clang_args=["-std=c++17", f"-I{tmp_path}"])
    defs = extract_definitions(tu)
    # Декларация foo в классе не выдаётся, только одна функция foo
    assert defs.count(("function", "foo", 4)) == 1

