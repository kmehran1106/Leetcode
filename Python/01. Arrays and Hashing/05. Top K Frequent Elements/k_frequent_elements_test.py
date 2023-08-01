"""
Problem Statement:
    https://leetcode.com/problems/top-k-frequent-elements/submissions/
"""


import pytest
from typing import List, NamedTuple

from k_frequent_elements import Solution


class InputTuple(NamedTuple):
    nums: List[int]
    k: int


@pytest.fixture
def get_fixtures():
    first_input = InputTuple(nums=[1, 1, 1, 2, 2, 3], k=2)
    first_output = [1, 2]

    second_input = InputTuple(nums=[1], k=1)
    second_output = [1]

    third_input = InputTuple(nums=[-1, -1], k=1)
    third_output = [-1]

    fourth_input = InputTuple(nums=[3,0,1,0], k=1)
    fourth_output = [0]

    return [
        (first_input, first_output),
        (second_input, second_output),
        (third_input, third_output),
        (fourth_input, fourth_output)
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert Solution().solution_one(*data[0]) == data[1]
        assert Solution().solution_two(*data[0]) == data[1]
