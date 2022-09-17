import pytest

from maximum_sum_of_continous_subarray_index import Solution


@pytest.fixture
def get_fixtures():
    first_input = [-1, 9, 0, 8, -5, 6, -24]
    first_output_sum = 18
    first_output_index = [1, 5]

    second_input = [-722, 713, 83, -285, -39, 860, -505, -775, -389, 584]
    second_output_sum = 1332
    second_output_index = [1, 5]

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
    third_output_sum = -504
    third_output_index = [5, 5]

    return [
        (first_input, first_output_sum, first_output_index),
        (second_input, second_output_sum, second_output_index),
        (third_input, third_output_sum, third_output_index),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert Solution().execute_with_sum(data[0]) == data[1]
        assert Solution().execute_with_index(data[0]) == data[2]
