# NOTE: PROBLEM STATEMENT - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List


class Solution:
    def execute(self, prices: List[int]) -> int:
        start, end = 0, 1
        max_profit = 0

        while end < len(prices):
            if prices[start] < prices[end]:
                _profit = prices[end] - prices[start]
                max_profit = max(max_profit, _profit)
            else:
                start = end
            end += 1

        return max_profit

