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
            # NOTE: FIND OUT THE LENGTH BY SLICING UNTIL WE FIND THE DELIMITER #
            j = i
            while encoded_string[j] != "#":
                j += 1
            _len = int(encoded_string[i:j])

            # NOTE: GET THE STRING BY SLICING FROM J+1 UPTO J+1+LENGTH OF CURRENT WORD FOUND
            result.append(str(encoded_string[j+1:j+1+_len]))

            # NOTE: UPDATE INITIAL ITERATOR I FROM J+1+LENGTH
            i = j + 1 + _len

        return result

