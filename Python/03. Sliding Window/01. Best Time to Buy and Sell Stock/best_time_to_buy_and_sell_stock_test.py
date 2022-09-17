import pytest

from best_time_to_buy_and_sell_stock import Solution


@pytest.fixture
def get_fixtures():
    first_input = [7, 1, 5, 3, 6, 4]
    first_output = 5

    second_input = [7, 6, 4, 3, 1]
    second_output = 0

    third_input = [2,1,2,1,0,1,2]
    third_output = 2

    return [
        (first_input, first_output),
        (second_input, second_output),
        (third_input, third_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert Solution().execute(data[0]) == data[1]
