"""
Problem Statement:
    https://leetcode.com/problems/contains-duplicate/
"""


import pytest
from typing import List


class Solution:
    def execute(self, nums: List[int]) -> bool:
        _set = set()

        for num in nums:
            if num in _set:
                return True

            _set.add(num)

        return False


@pytest.fixture
def get_fixtures():
    first_input = [1, 2, 3, 4]
    first_output = False

    second_input = [1, 2, 3, 1]
    second_output = True

    return [
        (first_input, first_output),
        (second_input, second_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert Solution().execute(data[0]) == data[1]
