# NOTE: PROBLEM STATEMENT - https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def execute_with_size(self, string: int) -> int:
        hashset, max_length = set(), 0

        for index, char in enumerate(string):

            if char not in hashset:
                hashset.add(char)
                _cur_length = len(hashset)
                max_length = max(_cur_length, max_length)
            else:
                hashset = set()

        return max_length

    def execute_with_index(self, string: int) -> int:
        hashset, max_length = set(), 0

        start, end, i = 0, 0, 0

        for index, char in enumerate(string):

            if char not in hashset:
                hashset.add(char)
                _cur_length = len(hashset)

                if _cur_length > max_length:
                    max_length = _cur_length
                    end = index
                    start = i
            else:
                hashset = set()
                i = index + 1

        return (end - start) + 1
