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

    return [
        (first_input, first_output),
        (second_input, second_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert Solution().solution_one(*data[0]) == data[1]
        assert Solution().solution_two(*data[0]) == data[1]
