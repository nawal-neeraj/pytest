from tabnanny import check
from unittest.mock import MagicMock, Mock, ANY


def production(a: int = 2):
    if a%2!=0:
       return "even"
    return "odd"


def test_productionClass():
    check = MagicMock(return_value=24)
    check()
    val = production(check.return_value)
    assert val == "odd"
    
def test_random():
    check = MagicMock()
    check(1,2,3)
    assert check == ANY
