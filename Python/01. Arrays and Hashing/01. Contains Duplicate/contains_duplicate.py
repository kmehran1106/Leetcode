# NOTE: Problem Statement: https://leetcode.com/problems/contains-duplicate/


from typing import List


class Solution:
    def execute(self, nums: List[int]) -> bool:
        _set = set()

        for num in nums:
            if num in _set:
                return True

            _set.add(num)

        return False
