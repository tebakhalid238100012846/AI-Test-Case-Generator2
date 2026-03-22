# This file will contain the test generator.
from pathlib import Path
import ast

SOURCE_FILE = "target_code.py"
TEST_FILE = "test_generated.py"

def get_function_names(source_code: str):
    tree = ast.parse(source_code)
    return [node.name for node in tree.body if isinstance(node, ast.FunctionDef)]

def build_tests(function_names):
    lines = []
    lines.append("import pytest")
    lines.append("from target_code import *")
    lines.append("")
    
    if "add" in function_names:
        lines.append("def test_add():")
        lines.append("    assert add(2, 3) == 5")
        lines.append("    assert add(-1, 1) == 0")
        lines.append("    assert add(0, 0) == 0")
        lines.append("")
    
    if "subtract" in function_names:
        lines.append("def test_subtract():")
        lines.append("    assert subtract(5, 3) == 2")
        lines.append("    assert subtract(0, 5) == -5")
        lines.append("    assert subtract(-2, -2) == 0")
        lines.append("")
    
    if "multiply" in function_names:
        lines.append("def test_multiply():")
        lines.append("    assert multiply(2, 3) == 6")
        lines.append("    assert multiply(-2, 3) == -6")
        lines.append("    assert multiply(0, 10) == 0")
        lines.append("")
    
    if "divide" in function_names:
        lines.append("def test_divide():")
        lines.append("    assert divide(6, 3) == 2")
        lines.append("    assert divide(5, 2) == 2.5")
        lines.append("    with pytest.raises(ZeroDivisionError):")
        lines.append("        divide(5, 0)")
        lines.append("")
    
    if "is_even" in function_names:
        lines.append("def test_is_even():")
        lines.append("    assert is_even(100) is True")
        lines.append("    assert is_even(101) is False")
        lines.append("    assert is_even(0) is True")
        lines.append("")
    
    if "factorial" in function_names:
        lines.append("def test_factorial():")
        lines.append("    assert factorial(0) == 1")
        lines.append("    assert factorial(1) == 1")
        lines.append("    assert factorial(5) == 120")
        lines.append("    with pytest.raises(ValueError):")
        lines.append("        factorial(-1)")
        lines.append("    with pytest.raises(TypeError):")
        lines.append("        factorial(2.5)")
        lines.append("")
    
    if len(lines) == 3:
        lines.append("def test_placeholder():")
        lines.append("    assert True")
        lines.append("")
    
    return "\n".join(lines)

def generate_test_file(source_file=SOURCE_FILE, test_file=TEST_FILE):
    source_code = Path(source_file).read_text(encoding="utf-8")
    function_names = get_function_names(source_code)
    test_code = build_tests(function_names)
    Path(test_file).write_text(test_code, encoding="utf-8")
    print(f"Generated {test_file} successfully")
    print("\n===== GENERATED TESTS =====\n")
    print(test_code)

if __name__ == "__main__":
    generate_test_file()
