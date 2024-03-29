import pytest
from typing import List, NamedTuple

from subarray_sum_equals_k import Solution


class InputTuple(NamedTuple):
    nums: List[int]
    k: int


@pytest.fixture
def get_fixtures():
    first_input = InputTuple(nums=[1, 1, 1], k=2)
    first_output = 2

    second_input = InputTuple(nums=[1, 2, 3, 4, 5], k=9)
    second_output = 2

    third_input = InputTuple(nums=[-1, -1, 1], k=0)
    third_output = 1

    fourth_input = InputTuple(nums=[1, -1, 0], k=0)
    fourth_output = 3

    fifth_input = InputTuple(nums=[1, 2, 1, 2, 1], k=3)
    fifth_output = 4

    return [
        (first_input, first_output),
        (second_input, second_output),
        (third_input, third_output),
        (fourth_input, fourth_output),
        (fifth_input, fifth_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert Solution().execute_brute_force(*data[0]) == data[1]
        assert Solution().execute_prefix_sum(*data[0]) == data[1]
