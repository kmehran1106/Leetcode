import pytest
from typing import List


class Solution:
    def execute(self, sentence: str) -> List[str]:
        x = list()

        sentence = sentence.split(" ")
        longest = 0
        for word in sentence:
            _len = len(word)
            longest = _len if _len > longest else longest

        for i in range(longest):
            _w = ""
            for word in sentence:
                _w = _w + word[i] if len(word) > i else _w + " "
            x.append(_w.rstrip())

        return x


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
