# NOTE: Problem Statement: https://leetcode.com/problems/top-k-frequent-elements/submissions/


from typing import List


class Solution:
    def solution_one(self, nums: List[int], k: int) -> List[int]:
        _map = dict()
        for num in nums:
            _map[num] = 1 + _map.get(num, 0)

        _map = dict(sorted(_map.items(), key=lambda x: x[1], reverse=True))

        return list(_map.keys())[0:k]

    def solution_two(self, nums: List[int], t: int) -> List[int]:
        _map = dict()
        for num in nums:
            _map[num] = 1 + _map.get(num, 0)

        _temp = [[]] * (len(nums) + 1)
        for k, v in _map.items():
            _temp[v].append(k)

        _result = list()
        for l in _temp[::-1]:
            _result.extend(l)

        return _result[0:t]
