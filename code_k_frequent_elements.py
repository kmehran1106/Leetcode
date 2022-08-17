"""
Problem Statement:
    https://leetcode.com/problems/top-k-frequent-elements/submissions/
"""


import pytest
from typing import List, NamedTuple


class Solution:
    def solution_one(self, nums: List[int], k: int) -> List[int]:
        _map = dict()
        for num in nums:
            _map[num] = 1 + _map.get(num, 0)

        _map = dict(sorted(_map.items(), key=lambda x: x[1], reverse=True))

        return list(_map.keys())[0:k]

    def solution_two(self, nums: List[int], t: int) -> List[int]:
        _map = dict()
        for num in nums:
            _map[num] = 1 + _map.get(num, 0)

        _temp = [[] for i in range(len(nums) + 1)]
        for k, v in _map.items():
            _temp[v].append(k)

        _result = list()
        for l in _temp[::-1]:
            _result.extend(l)

        return _result[0:t]


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
