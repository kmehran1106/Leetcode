"""
Problem Statement:
    https://leetcode.com/problems/two-sum/
"""


import pytest
from typing import List, NamedTuple


class Solution:
    def execute(self, nums: List[int], target: int) -> List[int]:
        _hashmap = dict()
        for a, value in enumerate(nums):
            b = _hashmap.get(target - value, None)
            if b is None:
                _hashmap[value] = a
            else:
                return [b, a]
        return list()


class InputTuple(NamedTuple):
    nums: List[int]
    target: int


@pytest.fixture
def get_fixtures():
    first_input = InputTuple(nums=[2, 7, 11, 15], target=9)
    first_output = [0, 1]

    second_input = InputTuple(nums=[3, 2, 4], target=6)
    second_output = [1, 2]

    return [
        (first_input, first_output),
        (second_input, second_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert Solution().execute(*data[0]) == data[1]
