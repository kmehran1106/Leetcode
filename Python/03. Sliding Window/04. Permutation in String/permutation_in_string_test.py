import pytest

from permutation_in_string import Solution


@pytest.fixture
def get_fixtures():
    first_input = ("ab", "eidbaooo")
    first_output = True

    second_input = ("ab", "eidboaoo")
    second_output = False

    third_input = ("adc", "dcda")
    third_output = True

    return [
        (first_input, first_output),
        (second_input, second_output),
        (third_input, third_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert Solution().execute_with_anagram(*data[0]) == data[1]
        assert Solution().execute_with_hashmap(*data[0]) == data[1]
