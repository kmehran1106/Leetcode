# NOTE: PROBLEM STATEMENT - https://leetcode.com/problems/maximum-product-subarray/

from typing import List


class Solution:
    def execute(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        prefix, result, negative = 1, 0, -float("inf")

        for num in nums:
            prefix *= num

            if prefix > 0:
                result = max(prefix, result)
            elif prefix == 0:
                prefix = 1
                negative = -float("inf")
            else:
                if prefix > negative:
                    negative = prefix
                else:
                    result = max(prefix/negative, result)

        return int(result)
