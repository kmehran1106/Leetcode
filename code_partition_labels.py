"""
Problem Statement:
    https://leetcode.com/problems/partition-labels/
"""

import pytest
from typing import List, NamedTuple


class Solution:
    def execute(self, string: str) -> List[int]:
        _last = dict()
        _result = list()

        for i, c in enumerate(string):
            _last[c] = i

        _size, _pointer = 0, 0
        for i, c in enumerate(string):
            _size += 1
            _pointer = max(_pointer, _last[c])
            if i == _pointer:
                _result.append(_size)
                _size = 0

        return _result


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
