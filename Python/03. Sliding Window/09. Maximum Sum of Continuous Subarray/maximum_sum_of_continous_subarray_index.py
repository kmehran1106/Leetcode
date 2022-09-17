from typing import List


class Solution:
    def execute_with_sum(self, numbers: List[int]) -> List[int]:
        _max = numbers[0]
        _sum = 0

        for index, number in enumerate(numbers):
            _sum += number

            if _sum > _max:
                _max = _sum

            if _sum < 0:
                _sum = 0

        return _max

    def execute_with_index(self, numbers: List[int]) -> List[int]:
        _max = numbers[0]
        _sum = 0

        start, end, i = 0, 0, 0

        for index, number in enumerate(numbers):
            _sum += number

            if _sum > _max:
                _max = _sum
                end = index
                start = i

            if _sum < 0:
                _sum = 0
                i = index + 1

        return [start, end]
