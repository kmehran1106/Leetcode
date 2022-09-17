import pytest

from manatal_problem import Solution


@pytest.fixture
def get_fixtures():
    first_input = [-1, 9, 0, 8, -5, 6, -24]
    first_output = [1, 5]

    second_input = [-722, 713, 83, -285, -39, 860, -505, -775, -389, 584]
    second_output = [1, 5]

    third_input = [
        -622,
        -812,
        -719,
        -715,
        -596,
        -504,
        -890,
        -532,
        -837,
        -853,
        -817,
        -623,
        -594,
        -988,
        -935,
        -869,
        -965,
        -674,
        -591,
        -920,
    ]
    third_output = [5, 5]

    return [
        (first_input, first_output),
        (second_input, second_output),
        (third_input, third_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert Solution().execute(data[0]) == data[1]
