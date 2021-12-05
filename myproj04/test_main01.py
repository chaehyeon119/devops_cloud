import pytest
from main01 import get_word_count, get_ch_count_except_space


@pytest.mark.parametrize(
    "sentence, expected",
    [
        ("우리는 파이썬을 즐겨요", 3),
        ("Python Family", 2),
    ],
)
def test_get_word_count(sentence, expected):
    assert get_word_count(sentence) == expected


@pytest.mark.parametrize(
    "sentence, expected",
    [("우리는 파이썬을 즐겨요", 3), ("Python Family", 2)],
)
def test_get_ch_count_except_space(sentence, expected):
    assert get_ch_count_except_space(sentence) == expected
