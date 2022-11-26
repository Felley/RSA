import pytest
from RSA import encode, decode


def test_encode_decode():
    tests = [
        (
            37, 47, 523, "merry christmas",
            [170, 1228, 979, 979, 619, 553, 1401, 898, 979, 973, 576, 718, 170, 1224, 576]
        ),
        (
            37, 47, 523, "alan turing",
            [1224, 874, 1224, 682, 553, 718, 1346, 979, 973, 682, 897]
        ),
        (
            47, 83, 2995, "good morning",
            [3401, 3277, 3277, 2371, 79, 3427, 3277, 1509, 2497, 2943, 2497, 3401]
        ),
        # TODO: CHECK WHY HERE WE CAN'T INVERT K
        # (
        #     67, 79, 2827, "have a nice day",
        #     [4995, 669, 2078, 4326, 834, 669, 834, 573, 2048, 4823, 4326, 834, 2181, 669, 3885]
        # ),
        (
            29, 53, 515, "yandex school of data analysis",
            [562, 595, 837, 908, 168, 710, 482, 55, 1086, 872, 534, 534, 1052, 482, 534, 496, 482, 908, 595, 586, 595,
             482, 595, 837, 595, 1052, 562, 55, 1315, 55]
        ),
        (
            79, 97, 5971, "math models in information technologies",
            [409, 7661, 7447, 599, 4756, 409, 5749, 5814, 2260, 5034, 3143, 4756, 2159, 7550, 4756, 2159, 7550, 1094,
             5749, 5871, 409, 7661, 7447, 2159, 5749, 7550, 4756, 7447, 2260, 3627, 599, 7550, 5749, 5034, 5749, 4,
             2159, 2260, 3143]
        ),
    ]

    for (p, q, k, letter, cypher) in tests:
        assert encode(p, q, k, letter) == cypher
        assert decode(p * q, k, cypher) == letter