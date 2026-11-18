import pytest

@pytest.mark.parametrize(
    "username, expected",
    [
        ("Gaurav", True),
        ("Ram", True),
        ("ABC", False),
        ("", False)
    ]
)
def test_username_validation(username, expected):
    is_valid = len(username) >= 3
    assert is_valid == expected