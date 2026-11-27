import pytest

from utils import count_vowels


@pytest.mark.parametrize(
    "text, expected",
    [("", 0), ("aeiouAEIOU", 10), ("rhythms 123!", 0),
     ("Hello WORLD!", 3), ("Beautiful day", 6)],
)
def test_count_vowels(text, expected):
    assert count_vowels(text) == expected
