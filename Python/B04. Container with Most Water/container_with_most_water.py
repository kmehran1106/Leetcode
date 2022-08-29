# NOTE: PROBLEM STATEMENT - https://leetcode.com/problems/container-with-most-water/


from typing import List


class Solution:
    def execute(self, heights: List[int]) -> int:
        _result = 0
        l, r = 0, len(heights) - 1

        while l < r:
            _area = (r - l) * min(heights[l], heights[r])
            _result = max(_result, _area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return _result
