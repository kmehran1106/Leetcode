"""
Problem Statement:
    https://leetcode.com/problems/reshape-the-matrix/
"""


import pytest
from typing import List, NamedTuple
from collections import defaultdict


class Solution:
    def execute_brute_force(self, nums: List[int], k: int) -> int:
        result = 0

        for index, a in enumerate(nums):
            _sum = a

            if _sum == k:
                result += 1

            for b in nums[index+1:]:
                _sum += b
                if _sum == k:
                    result += 1

        return result

    def execute_prefix_sum(self, nums: List[int], k: int) -> int:
        result = 0

        _prefix_list = list()
        _prefix_dict = defaultdict(int)

        _prefix_sum = 0
        for num in nums:
            _prefix_sum += num
            _prefix_list.append(_prefix_sum)

        for _prefix_sum in _prefix_list:

            if _prefix_sum == k:
                result += 1

            _lookback = _prefix_dict.get(_prefix_sum - k, 0)
            if _lookback:
                result += _lookback

            _prefix_dict[_prefix_sum] += 1

        return result


class InputTuple(NamedTuple):
    nums: List[int]
    k: int


@pytest.fixture
def get_fixtures():
    first_input = InputTuple(nums=[1, 1, 1], k=2)
    first_output = 2

    second_input =  InputTuple(nums=[1, 2, 3, 4, 5], k=9)
    second_output = 2

    third_input =  InputTuple(nums=[-1, -1, 1], k=0)
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
