# NOTE: PROBLEM STATEMENT - https://leetcode.com/problems/valid-palindrome/


class Solution:
    def _is_alpha_numeric(self, c: str) -> bool:
        return ord("A") <= ord(c) <= ord("Z") or \
            ord("a") <= ord(c) <= ord("z") or \
            ord("0") <= ord(c) <= ord("9")

    def execute(self, s: str) -> bool:
        _s = ""

        # NOTE: REMOVE NON ALPHA NUMERIC CHARACTERS
        for c in s:
            _s = _s + c.lower() if self._is_alpha_numeric(c) else _s

        # NOTE: START A TWO POINTER PROCESS
        l, r = 0, len(_s) - 1
        while l < r:
            if _s[l] != _s[r]:
                return False
            else:
                l += 1
                r -= 1

        return True
