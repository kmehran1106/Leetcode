# NOTE: PROBLEM STATEMENT - https://leetcode.com/problems/print-words-vertically/


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
