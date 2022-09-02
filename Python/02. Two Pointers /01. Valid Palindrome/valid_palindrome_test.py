import pytest

from valid_palindrome import Solution


@pytest.fixture
def get_fixtures():
    first_input = "A man, a plan, a canal: Panama"
    first_output = True

    second_input = "race a car"
    second_output = False

    return [
        (first_input, first_output),
        (second_input, second_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert Solution().execute(data[0]) == data[1]
