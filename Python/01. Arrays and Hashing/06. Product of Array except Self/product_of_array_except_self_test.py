"""
Problem Statement:
    https://leetcode.com/problems/top-k-frequent-elements/submissions/
"""


import pytest

from product_of_array_except_self import Solution


@pytest.fixture
def get_fixtures():
    first_input = [1, 2, 3, 4]
    first_output = [24, 12, 8, 6]

    second_input = [-1, 1, 0, -3, 3]
    second_output = [0, 0, 9, 0, 0]

    return [
        (first_input, first_output),
        (second_input, second_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert Solution().solution_basic(data[0]) == data[1]
        assert Solution().solution_follow_up(data[0]) == data[1]
