import pytest

from merge_sort import Solution


@pytest.fixture
def get_fixtures():
    first_input = [1, 2, 3, 4, 5, 6]
    first_output = [1, 2, 3, 4, 5, 6]

    second_input = [2, 4, 3, 0, 1, 9]
    second_output = [0, 1, 2, 3, 4, 9]

    return [
        (first_input, first_output),
        (second_input, second_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert Solution().execute(data[0]) == data[1]
