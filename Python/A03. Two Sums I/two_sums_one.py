# NOTE: PROBLEM STATEMENT - https://leetcode.com/problems/two-sum/

from typing import List


class Solution:
    def execute(self, nums: List[int], target: int) -> List[int]:
        _hashmap = dict()
        for index, value in enumerate(nums):
            a = target - value
            b = _hashmap.get(a, None)

            if b is not None:
                return [b, index]
            else:
                _hashmap[value] = index

        return list()
