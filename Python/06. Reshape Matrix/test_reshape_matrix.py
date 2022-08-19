import pytest
from typing import List, NamedTuple

from reshape_matrix import Solution


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
