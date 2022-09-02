import pytest

from template import Solution


@pytest.fixture
def get_fixtures():
    first_input = 0
    first_output = 0

    second_input = 0
    second_output = 0

    third_input = 0
    third_output = 0

    return [
        (first_input, first_output),
        (second_input, second_output),
        (third_input, third_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert Solution().execute(data[0]) == data[1]
