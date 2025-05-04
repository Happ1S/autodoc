import ast
from typing import List, Tuple

# Definition = (тип, имя, номер строки)
Definition = Tuple[str, str, int]

def parse_file(path: str) -> ast.Module:
    with open(path, 'r', encoding='utf-8') as f:
        source = f.read()
    return ast.parse(source, filename=path)

def extract_definitions(module: ast.Module) -> List[Definition]:
    defs: List[Definition] = []
    for node in module.body:
        if isinstance(node, ast.ClassDef):
            defs.append(("class", node.name, node.lineno))
            for child in node.body:
                if isinstance(child, ast.FunctionDef):
                    defs.append(("method", f"{node.name}.{child.name}", child.lineno))
        elif isinstance(node, ast.FunctionDef):
            defs.append(("function", node.name, node.lineno))
    return defs
