# NOTE: PROBLEM STATEMENT - https://leetcode.com/problems/3sum/

from typing import List


class Solution:
    def execute(self, nums: List[int]) -> List[List[int]]:
        _result = list()

        nums.sort()

        for index, num in enumerate(nums):
            # NOTE: IGNORE IF NUM EQUALS EARLIER VALUE
            if index > 0 and num == nums[index - 1]:
                continue

            # NOTE: START A TWO POINTER PROCESS FROM INDEX AND CHECK IF L + R EQUALS NUM
            l, r = index + 1, len(nums) - 1

            while l < r:
                threesum = num + nums[l] + nums[r]

                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    _result.append([num, nums[l], nums[r]])
                    l += 1

                    # NOTE: IF THE NEXT VALUE IS SAME AS PREVIOUS VALUE OF NUMS[L], THERE WILL BE DUPLICATE ENTRIES
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return _result
