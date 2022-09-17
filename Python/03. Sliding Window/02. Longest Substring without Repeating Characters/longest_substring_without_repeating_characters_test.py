import pytest

from longest_substring_without_repeating_characters import Solution


@pytest.fixture
def get_fixtures():
    first_input = "abcabcbb"
    first_output = 3

    second_input = "bbbbb"
    second_output = 1

    third_input = "pwwkew"
    third_output = 3

    return [
        (first_input, first_output),
        (second_input, second_output),
        (third_input, third_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert Solution().execute_with_size(data[0]) == data[1]
        assert Solution().execute_with_index(data[0]) == data[1]
