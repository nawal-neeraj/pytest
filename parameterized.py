import pytest

def sum_number(a,b):
    return a + b

@pytest.mark.parametrize("a, b, expected", [(10, 10, 20), (10, 0, 10), (0, 0, 0), (10, -10, 0)])
def test_sum_number(a, b, expected):
    print(f"a: {a}, b: {b}, expected: {expected}")
    assert sum_number(a,b) == expected
    
def convert_upper_case(input):
    return input.upper()

@pytest.mark.parametrize("input, expected", [("pytest python", "PYTEST PYTHON"),("AbCd", "ABCD"), ("ABCD", "ABCD")])
def test_convert_upper_case(input, expected):
    assert convert_upper_case(input) == expected

