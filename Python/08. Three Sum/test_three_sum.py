import pytest

from three_sum import Solution


@pytest.fixture
def get_fixtures():
    first_input = [-1, 0, 1, 2, -1, -4]
    first_output = [[-1, -1, 2], [-1, 0, 1]]

    second_input = []
    second_output = []

    third_input = [0]
    third_output = []

    fourth_input = [0, 0, 0, 0]
    fourth_output = [[0, 0, 0]]

    fifth_input = [-3, 3, 4, -3, -3, 1, 2]
    fifth_output = [[-3, 1, 2]]

    return [
        (first_input, first_output),
        (second_input, second_output),
        (third_input, third_output),
        (fourth_input, fourth_output),
        (fifth_input, fifth_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert Solution().execute(data[0]) == data[1]
