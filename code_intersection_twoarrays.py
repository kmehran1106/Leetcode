"""
Problem Statement:
    https://leetcode.com/problems/reshape-the-matrix/
"""


import pytest
from typing import List, NamedTuple
from common_binary_search import Solution as BinarySearch


class Solution:
    def execute(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        result = list()

        for v in nums1:
            _index = BinarySearch().execute(nums2, v)
            if _index != -1 and result.count(v) < nums2.count(v):
                result.append(nums2[_index])

        result.sort()
        return result


class InputTuple(NamedTuple):
    nums1: List[int]
    nums2: List[int]


@pytest.fixture
def get_fixtures():
    first_input = InputTuple(nums1=[1, 2, 2, 1], nums2=[2, 2])
    first_output = [2, 2]

    second_input = InputTuple(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4])
    second_output = [4, 9]

    third_input = InputTuple(nums1=[1, 2, 2, 1], nums2=[2])
    third_output = [2]

    fourth_input = InputTuple(
        nums1=[
            21,
            47,
            80,
            4,
            3,
            24,
            87,
            12,
            22,
            11,
            48,
            6,
            89,
            80,
            74,
            71,
            74,
            55,
            58,
            56,
            4,
            98,
            40,
            66,
            49,
            53,
            62,
            27,
            3,
            66,
            78,
            24,
            48,
            69,
            88,
            12,
            80,
            63,
            98,
            65,
            46,
            35,
            72,
            5,
            64,
            72,
            7,
            29,
            37,
            3,
            2,
            75,
            44,
            93,
            79,
            78,
            13,
            39,
            85,
            26,
            15,
            41,
            87,
            47,
            29,
            93,
            41,
            74,
            6,
            48,
            17,
            89,
            27,
            61,
            2,
            68,
            99,
            57,
            45,
            73,
            25,
            33,
            38,
            32,
            58,
        ],
        nums2=[
            1,
            39,
            6,
            81,
            85,
            10,
            38,
            22,
            0,
            89,
            57,
            93,
            58,
            69,
            65,
            80,
            84,
            24,
            27,
            54,
            37,
            36,
            26,
            88,
            2,
            7,
            24,
            36,
            51,
            5,
            74,
            57,
            45,
            56,
            55,
            67,
            25,
            33,
            78,
            49,
            16,
            79,
            74,
            80,
            36,
            27,
            89,
            49,
            64,
            73,
            96,
            60,
            92,
            31,
            98,
            72,
            22,
            31,
            0,
            93,
            70,
            87,
            80,
            66,
            75,
            69,
            81,
            52,
            94,
            90,
            51,
            90,
            74,
            36,
            58,
            38,
            50,
            9,
            64,
            55,
            4,
            21,
            49,
            60,
            65,
            47,
            67,
            8,
            38,
            83,
        ],
    )
    fourth_output = [
        21,
        47,
        80,
        4,
        24,
        87,
        22,
        6,
        89,
        80,
        74,
        74,
        55,
        58,
        56,
        98,
        66,
        49,
        27,
        78,
        24,
        69,
        88,
        80,
        65,
        72,
        5,
        64,
        7,
        37,
        2,
        75,
        93,
        79,
        39,
        85,
        26,
        93,
        74,
        89,
        27,
        57,
        45,
        73,
        25,
        33,
        38,
        58,
    ]

    first_output.sort()
    second_output.sort()
    third_output.sort()
    fourth_output.sort()

    return [
        (first_input, first_output),
        (second_input, second_output),
        (third_input, third_output),
        (fourth_input, fourth_output),
    ]


def test_code(get_fixtures):
    for data in get_fixtures:
        assert Solution().execute(*data[0]) == data[1]
