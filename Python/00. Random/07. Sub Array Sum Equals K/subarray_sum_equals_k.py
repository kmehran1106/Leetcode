# NOTE: PROBLEM STATEMENT - https://leetcode.com/problems/subarray-sum-equals-k/


from typing import List
from collections import defaultdict


class Solution:
    def execute_brute_force(self, nums: List[int], k: int) -> int:
        result = 0

        for index, a in enumerate(nums):
            _sum = a

            if _sum == k:
                result += 1

            for b in nums[index + 1 :]:
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
