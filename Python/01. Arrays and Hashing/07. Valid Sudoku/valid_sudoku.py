# NOTE: Problem Statement - https://leetcode.com/problems/top-k-frequent-elements/submissions/


import collections
from typing import List


class Solution:
    def execute(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                elif board[r][c] in rows[r]:
                    return False
                elif board[r][c] in cols[c]:
                    return False
                elif board[r][c] in boxes[(r // 3, c // 3)]:
                    return False
                else:
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    boxes[(r // 3, c // 3)].add(board[r][c])

        return True
