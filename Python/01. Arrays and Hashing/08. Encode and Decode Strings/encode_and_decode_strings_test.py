import pytest

from encode_and_decode_strings import Solution


@pytest.fixture
def get_fixtures():
    first_strings = ["life", "is", "hard"]
    second_strings = ["#good", "#game", "#well", "#played"]

    return [
        first_strings,
        second_strings,
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        _encoded = Solution().encode(data)
        _decoded = Solution().decode(_encoded)
        assert _decoded == data
