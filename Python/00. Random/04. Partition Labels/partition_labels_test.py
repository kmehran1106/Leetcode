import pytest
from typing import List, NamedTuple

from partition_labels import Solution


class InputTuple(NamedTuple):
    string: str


@pytest.fixture
def get_fixtures():
    first_input = InputTuple(string="ababcbacadefegdehijhklij")
    first_output = [9, 7, 8]

    second_input = InputTuple(string="eccbbbbdecf")
    second_output = [10, 1]

    third_input = InputTuple(string="abcabd")
    third_output = [5, 1]

    return [
        (first_input, first_output),
        (second_input, second_output),
        (third_input, third_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert Solution().execute(*data[0]) == data[1]
