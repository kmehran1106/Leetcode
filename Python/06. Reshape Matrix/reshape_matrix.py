# NOTE: PROBLEM STATEMENT - https://leetcode.com/problems/reshape-the-matrix/


from typing import List


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
