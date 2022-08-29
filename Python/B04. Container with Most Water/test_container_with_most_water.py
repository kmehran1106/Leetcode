import pytest

from container_with_most_water import Solution


@pytest.fixture
def get_fixtures():
    first_input = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    first_output = 49

    second_input = [1, 1]
    second_output = 1

    return [
        (first_input, first_output),
        (second_input, second_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert Solution().execute(data[0]) == data[1]
