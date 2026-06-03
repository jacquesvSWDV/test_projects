import pytest

#use what is called a decorator
@pytest.fixture
def simple_list():
    return [1, 2, 3, 4, 5]

@pytest.fixture
def simple_dict():
    return {"name": "Bryan", "age": 30}

