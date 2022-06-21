"""
Problem Statement:
    https://leetcode.com/problems/3sum/
"""


import pytest
from typing import List


class Solution:
    def execute(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        x = list()

        for i, value in enumerate(nums):
            if i > 0 and value == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                threesum = value + nums[l] + nums[r]

                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    x.append([value, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return x


@pytest.fixture
def get_fixtures():
    first_input = [-1, 0, 1, 2, -1, -4]
    first_output = [[-1, -1, 2], [-1, 0, 1]]

    second_input = []
    second_output = []

    third_input = [0]
    third_output = []

    fourth_input = [0, 0, 0, 0]
    fourth_output = [[0, 0, 0]]

    fifth_input = [-3, 3, 4, -3, -3, 1, 2]
    fifth_output = [[-3, 1, 2]]

    return [
        (first_input, first_output),
        (second_input, second_output),
        (third_input, third_output),
        (fourth_input, fourth_output),
        (fifth_input, fifth_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert Solution().execute(data[0]) == data[1]
