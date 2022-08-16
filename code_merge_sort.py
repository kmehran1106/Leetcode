import pytest
from typing import List
from copy import deepcopy


class Solution:
    def _merge_sort(self, arr: List[int]):
        if len(arr) > 1:
            _mid = len(arr) // 2
            left_arr = arr[:_mid]
            right_arr = arr[_mid:]

            self._merge_sort(left_arr)
            self._merge_sort(right_arr)

            i, j, k = 0, 0, 0

            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] <= right_arr[j]:
                    arr[k] = left_arr[i]
                    i += 1
                else:
                    arr[k] = right_arr[j]
                    j += 1
                k += 1

            while i < len(left_arr):
                arr[k] = left_arr[i]
                i += 1
                k += 1

            while j < len(right_arr):
                arr[k] = right_arr[j]
                j += 1
                k += 1

    def execute(self, arr: List[int]):
        _output = deepcopy(arr)
        self._merge_sort(_output)
        return _output


@pytest.fixture
def get_fixtures():
    first_input = [1, 2, 3, 4, 5, 6]
    first_output = [1, 2, 3, 4, 5, 6]

    second_input = [2, 4, 3, 0, 1, 9]
    second_output = [0, 1, 2, 3, 4, 9]

    return [
        (first_input, first_output),
        (second_input, second_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert Solution().execute(data[0]) == data[1]
