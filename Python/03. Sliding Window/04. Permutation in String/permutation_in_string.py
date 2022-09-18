# NOTE: PROBLEM STATEMENT -


class Solution:
    def _is_anagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # NOTE: POPULATE COUNT OF EACH CHARACTER THAT'S APPEARED IN THE STRING IN TWO SEPARATE HASHMAPS
        _map_s, _map_t = dict(), dict()
        for i in range(len(s)):
            _map_s[s[i]] = 1 + _map_s.get(s[i], 0)
            _map_t[t[i]] = 1 + _map_t.get(t[i], 0)

        # NOTE: CHECK IF THE COUNT OF EACH CHARACTER IN S IS SAME AS THE COUNT OF THAT CHARACTER IN T
        for k, v in _map_s.items():
            if v != _map_t.get(k, 0):
                return False
        return True

    def execute_with_anagram(self, s1: str, s2: str) -> bool:
        l = 0

        for r in range(len(s1), len(s2) + 1):
            t = s2[l:r]
            is_anagram = self._is_anagram(s1, t)
            if is_anagram:
                return True
            l += 1

        return False

    def _get_hashmap_counter(self, s: str) -> dict:
        _map = dict()

        for c in s:
            _map[c] = 1 + _map.get(c, 0)

        return _map

    def execute_with_hashmap(self, s1: str, s2: str) -> bool:
        l = 0
        _map_s1 = self._get_hashmap_counter(s1)

        for r in range(len(s1), len(s2) + 1):
            _map_window = self._get_hashmap_counter(s2[l:r])
            if _map_s1 == _map_window:
                return True
            l += 1

        return False
