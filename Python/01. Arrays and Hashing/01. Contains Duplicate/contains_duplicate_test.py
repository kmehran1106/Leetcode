import pytest

from contains_duplicate import Solution


@pytest.fixture
def get_fixtures():
    first_input = [1, 2, 3, 4]
    first_output = False

    second_input = [1, 2, 3, 1]
    second_output = True

    return [
        (first_input, first_output),
        (second_input, second_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert Solution().execute(data[0]) == data[1]
