import pytest
from fixtures import simple_list, simple_dict

#asserting item in list
def test_simple_list(simple_list):
    assert 3 in simple_list

#asserting values to keys in dictionary
@pytest.mark.example
def test_simple_dict(simple_dict):
    assert simple_dict["name"] == "Bryan"
    assert simple_dict["age"] == 30