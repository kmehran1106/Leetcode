# NOTE: PROBLEM STATEMENT - https://leetcode.com/problems/intersection-of-two-arrays-ii/


from typing import List


class Solution:
    def _binary_search(self, arr: List[int], value: int) -> int:
        low, high = 0, len(arr) - 1

        while low <= high:
            _mid = (high + low) // 2
            _value = arr[_mid]

            if _value < value:
                low = _mid + 1
            elif _value > value:
                high = _mid - 1
            else:
                return _mid

        return -1

    def solution_unsorted(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = list()

        map1 = dict()
        for n in nums1:
            map1[n] = 1 + map1.get(n, 0)

        for num in nums2:
            c = map1.get(num, None)
            if c and c > 0:
                result.append(num)
                map1[num] -= 1

        return result

    def solution_sorted(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        result = list()

        for v in nums1:
            _index = self._binary_search(nums2, v)
            if _index != -1 and result.count(v) < nums2.count(v):
                result.append(nums2[_index])

        result.sort()
        return result
