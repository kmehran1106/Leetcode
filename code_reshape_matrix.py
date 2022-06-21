"""
Problem Statement:
    https://leetcode.com/problems/reshape-the-matrix/
"""


import pytest
from typing import List, NamedTuple


class Solution:
    def execute(self, matrix: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(matrix) * len(matrix[0]) != r * c:
            return matrix

        _flattened, _matrix = list(), list()
        # _flattened = functools.reduce(lambda a, b: a + b, matrix, list())
        for _row in matrix:
            _flattened.extend(_row)

        i = 0
        for _ in range(r):
            _matrix.append(_flattened[i : i + c])
            i += c
        return _matrix


class InputTuple(NamedTuple):
    matrix: List[List[int]]
    r: int
    c: int


@pytest.fixture
def get_fixtures():
    first_input = InputTuple(matrix=[[1, 2], [3, 4]], r=1, c=4)
    first_output = [[1, 2, 3, 4]]

    second_input = InputTuple(matrix=[[1, 2], [3, 4]], r=2, c=4)
    second_output = [[1, 2], [3, 4]]

    return [
        (first_input, first_output),
        (second_input, second_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert Solution().execute(*data[0]) == data[1]
