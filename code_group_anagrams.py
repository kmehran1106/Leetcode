"""
Problem Statement:
    https://leetcode.com/problems/two-sum/
"""


import pytest
from collections import defaultdict
from typing import List


class Solution:
    def execute(self, strs: List[str]) -> List[List[str]]:
        _map = defaultdict(list)

        for word in strs:
            _s = [0] * 26
            for c in word:
                _s[ord(c) - ord("a")] += 1
            _map[tuple(_s)].append(word)

        return list(_map.values())


@pytest.fixture
def get_fixtures():
    first_input = ["eat", "tea", "tan", "ate", "nat", "bat"]
    first_output = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

    second_input = [""]
    second_output = [[""]]

    third_input = ["a"]
    third_output = [["a"]]

    return [
        (first_input, first_output),
        (second_input, second_output),
        (third_input, third_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        _result = Solution().execute(data[0])
        _expected = data[1]

        for r in _result:
            r.sort()
        _result.sort()

        for e in _expected:
            e.sort()
        _expected.sort()

        assert _result == _expected
