# NOTE: PROBLEM STATEMENT - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/


from typing import List


class Solution:
    def execute(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1

        while l < r:
            _sum = nums[l] + nums[r]

            if _sum > target:
                r -= 1
            elif _sum < target:
                l += 1
            else:
                return [l+1, r+1]

        return list()
