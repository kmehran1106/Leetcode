# NOTE: PROBLEM STATEMENT - https://leetcode.com/problems/encode-and-decode-strings/


import collections
from typing import List


class Solution:
    def encode(self, words: List[str]) -> str:
        result = ""

        for word in words:
            result += f"{len(word)}#{word}"

        return result

    def decode(self, encoded_string: str) -> List[str]:
        result = list()
        i = 0
        while i < len(encoded_string):
            j = i
            while encoded_string[j] != "#":
                j += 1

            _len = int(encoded_string[i:j])
            result.append(str(encoded_string[j+1:j+1+_len]))

            i = j + 1 + _len

        return result

