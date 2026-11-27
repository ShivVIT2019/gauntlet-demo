import pytest

from utils import reverse_string


@pytest.mark.parametrize(
    "text, expected",
    [("", ""), ("a", "a"), ("hello", "olleh"), ("Ab c!", "!c bA")],
)
def test_reverse_string(text, expected):
    assert reverse_string(text) == expected
