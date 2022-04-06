from ...crud_operation_dict import add_values
from unittest.mock import patch, MagicMock
import pytest


mock = MagicMock()

@pytest.mark.parametrize(
    "key_name, value_dict, expected", [("key_one", "value_one", True)]
)
async def test_set_value(key_name, value_dict, expected):
    import ipdb; ipdb.set_trace()
    value = await add_values(key_name, value_dict)
    assert value == expected
    