import pytest
from unittest.mock import MagicMock, Mock, ANY
from typing import  TypeVar


class Product:
    
    random_value = 23
    
    def odd_even(self, a: int = 2):
        if a%2!=0:
            return "even"
        return "odd"
    
    def random(self, value):
        if Product.random_value == ANY:
            return "matched"
        return "failed"
        
        

@pytest.mark.asyncio
def test_odd_even_check():
    check = MagicMock(return_value=24)
    prod_instance = Product()
    val = prod_instance.production(check.return_value)
    assert val == "odd"
    
def test_random():
    check = MagicMock()
    prod_instance = Product()
    val = prod_instance.random(check)
    assert val == "matched"
