import pytest

from longest_consecutive_sequence import Solution


@pytest.fixture
def get_fixtures():
    first_input = [100,4,200,1,3,2]
    first_output = 4

    second_input = [0,3,7,2,5,8,4,6,0,1]
    second_output = 9

    return [
        (first_input, first_output),
        (second_input, second_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert Solution().execute(data[0]) == data[1]
