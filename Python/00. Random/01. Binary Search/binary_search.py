from typing import List


class Solution:
    def _binary_search(self, arr: List[int], value: int) -> int:
        low, high = 0, len(arr) - 1

        while low <= high:
            _mid_index = (high + low) // 2
            _mid_value = arr[_mid_index]

            if _mid_value < value:
                low = _mid_index + 1
            elif _mid_value > value:
                high = _mid_index - 1
            else:
                return _mid_index

        return -1

    def execute(self, arr: List[int], value: int) -> int:
        return self._binary_search(arr, value)
