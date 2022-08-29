import pytest
from typing import List, NamedTuple

from two_sums_two import Solution


class InputTuple(NamedTuple):
    nums: List[int]
    target: int


@pytest.fixture
def get_fixtures():
    first_input = InputTuple(nums=[2, 7, 11, 15], target=9)
    first_output = [1, 2]

    second_input = InputTuple(nums=[2, 3, 4], target=6)
    second_output = [1, 3]

    return [
        (first_input, first_output),
        (second_input, second_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert Solution().execute(*data[0]) == data[1]
