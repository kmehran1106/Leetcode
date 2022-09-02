from typing import List


class Solution:
    def _merge_sort(self, arr: List[int]) -> List[int]:
        result = list()

        if len(arr) > 1:
            _mid = len(arr) // 2
            left_arr = arr[:_mid]
            right_arr = arr[_mid:]

            left_arr = self._merge_sort(left_arr)
            right_arr = self._merge_sort(right_arr)

            i, j = 0, 0

            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] <= right_arr[j]:
                    result.append(left_arr[i])
                    i += 1
                else:
                    result.append(right_arr[j])
                    j += 1

            while i < len(left_arr):
                result.append(left_arr[i])
                i += 1

            while j < len(right_arr):
                result.append(right_arr[j])
                j += 1

            return result
        else:
            return arr

    def execute(self, arr: List[int]) -> List[int]:
        return self._merge_sort(arr)
