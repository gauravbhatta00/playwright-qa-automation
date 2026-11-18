import pytest

@pytest.fixture
def username():
    return "Gaurav"

def test_username(username):
    assert username == "Gaurav"
    print("Username verified:", username)