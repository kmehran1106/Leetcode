# NOTE: PROBLEM STATEMENT - https://leetcode.com/problems/longest-consecutive-sequence/

from typing import List


class Solution:
    def execute(self, nums: List[int]) -> int:
        _set = set(nums)
        _result = 0

        for num in nums:
            _length = 0

            if (num - 1) not in _set:
                while (num + _length) in _set:
                    _length += 1
                _result = max(_length, _result)

        return _result
