from multiprocessing.context import assert_spawning
from testadd import add

def test_method():
    assert add(3) == 2