import pytest
from typing import List, NamedTuple

from binary_search import Solution


class InputTuple(NamedTuple):
    arr: List[int]
    value: int


@pytest.fixture
def get_fixtures():
    first_input = InputTuple(arr=[3, 4, 5, 6, 7, 8, 9], value=4)
    first_output = 1

    second_input = InputTuple(arr=[3, 4, 5, 6, 7, 8, 9], value=1)
    second_output = -1

    return [
        (first_input, first_output),
        (second_input, second_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert Solution().execute(*data[0]) == data[1]
