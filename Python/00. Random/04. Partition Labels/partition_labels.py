# NOTE: PROBLEM  STATEMENT - https://leetcode.com/problems/partition-labels/


from typing import List


class Solution:
    def execute(self, string: str) -> List[int]:
        _last = dict()
        _result = list()

        for i, c in enumerate(string):
            _last[c] = i

        _size, _pointer = 0, 0
        for i, c in enumerate(string):
            _size += 1
            _pointer = max(_pointer, _last[c])
            if i == _pointer:
                _result.append(_size)
                _size = 0

        return _result
