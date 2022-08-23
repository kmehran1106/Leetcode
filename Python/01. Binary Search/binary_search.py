from typing import List


class Solution:
    def _binary_search(self, arr: List[int], value: int) -> int:
        low, high = 0, len(arr) - 1

        while low <= high:
            _mid = (high + low) // 2
            _value = arr[_mid]

            if _value < value:
                low = _mid + 1
            elif _value > value:
                high = _mid - 1
            else:
                return _mid

        return -1

    def execute(self, arr: List[int], value: int) -> int:
        return self._binary_search(arr, value)
