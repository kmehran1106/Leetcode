import pytest
from typing import List, NamedTuple


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


class InputTuple(NamedTuple):
    arr: List[int]
    value: int


@pytest.fixture
def get_fixtures():
    first_input = InputTuple(arr=[3, 4, 5, 6, 7, 8, 9], value=4)
    first_output = 1

    second_input = InputTuple(arr=[3, 4, 5, 6, 7, 8, 9], value=1)
    second_output = -1

    return [
        (first_input, first_output),
        (second_input, second_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert Solution().execute(*data[0]) == data[1]
