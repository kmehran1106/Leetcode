"""
Problem Statement:
    https://leetcode.com/problems/valid-anagram/
"""


import pytest
from typing import List, NamedTuple


class Solution:
    def execute(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # NOTE: POPULATE COUNT OF EACH CHARACTER THAT'S APPEARED IN THE STRING IN TWO SEPARATE HASHMAPS
        _map_s, _map_t = dict(), dict()
        for i in range(len(s)):
            _map_s[s[i]] = 1 + _map_s.get(s[i], 0)
            _map_t[t[i]] = 1 + _map_t.get(t[i], 0)

        # NOTE: CHECK IF THE COUNT OF EACH CHARACTER IN S IS SAME AS THE COUNT OF THAT CHARACTER IN T
        for k, v in _map_s.items():
            if v != _map_t.get(k, 0):
                return False
        return True


class InputTuple(NamedTuple):
    s: str
    t: str


@pytest.fixture
def get_fixtures():
    first_input = InputTuple(s="anagram", t="nagaram")
    first_output = True

    second_input = InputTuple(s="rat", t="car")
    second_output = False

    return [
        (first_input, first_output),
        (second_input, second_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert Solution().execute(*data[0]) == data[1]
