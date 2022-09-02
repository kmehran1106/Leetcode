import pytest
from typing import List, NamedTuple

from valid_anagram import Solution


class InputTuple(NamedTuple):
    s: str
    t: str


@pytest.fixture
def get_fixtures():
    first_input = InputTuple(s="anagram", t="nagaram")
    first_output = True

    second_input = InputTuple(s="rat", t="car")
    second_output = False

    return [
        (first_input, first_output),
        (second_input, second_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert Solution().execute(*data[0]) == data[1]
