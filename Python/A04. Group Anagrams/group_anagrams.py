# NOTE: Problem Statement: https://leetcode.com/problems/two-sum/


from collections import defaultdict
from typing import List


class Solution:
    def execute(self, strs: List[str]) -> List[List[str]]:
        _map = defaultdict(list)

        for word in strs:
            _s = [0] * 26
            for c in word:
                _s[ord(c) - ord("a")] += 1
            _map[tuple(_s)].append(word)

        return list(_map.values())
