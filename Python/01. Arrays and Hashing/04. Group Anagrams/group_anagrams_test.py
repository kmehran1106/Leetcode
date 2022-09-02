import pytest

from group_anagrams import Solution


@pytest.fixture
def get_fixtures():
    first_input = ["eat", "tea", "tan", "ate", "nat", "bat"]
    first_output = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

    second_input = [""]
    second_output = [[""]]

    third_input = ["a"]
    third_output = [["a"]]

    return [
        (first_input, first_output),
        (second_input, second_output),
        (third_input, third_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        _result = Solution().execute(data[0])
        _expected = data[1]

        for r in _result:
            r.sort()
        _result.sort()

        for e in _expected:
            e.sort()
        _expected.sort()

        assert _result == _expected
