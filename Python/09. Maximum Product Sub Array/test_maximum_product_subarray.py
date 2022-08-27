import pytest

from maximum_product_subarray import Solution


@pytest.fixture
def get_fixtures():
    first_input = [2, 3, -2, 4]
    first_output = 6

    second_input = [3, -1, 4, 5]
    second_output = 20

    third_input = [-2, 0, -1]
    third_output = 0

    third_input = [-3, -1, -1]
    third_output = 3

    return [
        (first_input, first_output),
        (second_input, second_output),
        (third_input, third_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert Solution().execute(data[0]) == data[1]
