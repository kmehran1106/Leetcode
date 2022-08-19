import pytest

from print_words_vertically import Solution


@pytest.fixture
def get_fixtures():
    first_input = "HOW ARE YOU"
    first_output = ["HAY", "ORO", "WEU"]

    return [
        (first_input, first_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert Solution().execute(data[0]) == data[1]
