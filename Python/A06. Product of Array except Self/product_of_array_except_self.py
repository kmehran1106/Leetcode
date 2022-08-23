# NOTE: Problem Statement: https://leetcode.com/problems/top-k-frequent-elements/submissions/


from typing import List


class Solution:
    def solution_basic(self, nums: List[int]) -> List[int]:
        _len = len(nums)
        _prefix, _postfix, _output = [0] * _len, [0] * _len, [0] * _len

        for index, num in enumerate(nums):
            if index == 0:
                _prefix[index] = num
            else:
                _prefix[index] = _prefix[index - 1] * num

        for index, num in enumerate(nums[::-1]):
            if index == 0:
                _postfix[index] = num
            else:
                _postfix[index] = _postfix[index - 1] * num
        _postfix = _postfix[::-1]

        for index in range(_len):
            if index == 0:
                _output[index] = 1 * _postfix[index + 1]
            elif index == _len - 1:
                _output[index] = _prefix[index - 1] * 1
            else:
                _output[index] = _prefix[index - 1] * _postfix[index + 1]
        return _output

    def solution_follow_up(self, nums: List[int]) -> List[int]:
        _len = len(nums)
        _output = [0] * _len

        _prefix, _postfix = 1, 1

        for i in range(_len):
            _output[i] = _prefix
            _prefix *= nums[i]

        for i in range(_len, 0, -1):
            _output[i - 1] *= _postfix
            _postfix *= nums[i - 1]

        return _output
