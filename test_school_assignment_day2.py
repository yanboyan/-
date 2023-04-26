# -*- coding:utf-8 -*-
# pytest day2
# @Time : 2023/4/26 23:05
# @Author : Augustine
# @File : test_school_assignment_day2.py
# @Software: PyCharm
import null as null
import pytest


@pytest.mark.parametrize(
    "a,b,expected",
    [
        [null, null, "参数为非数字"],
        [null, 25, "参数为非数字"],
        [25, null, "参数为非数字"],
        ["m", 25, "参数为非数字"],
        [25, "m", "参数为非数字"],
        [25, 25, 50],
        [25, 99, 124],
        [99, 25, 124],
        [-25, -99, -124],
        [-99, -25, -124],
        [25, 100, "参数超出-99至99范围"],
        [100, 25, "参数超出-99至99范围"],
        [-25, -100, "参数超出-99至99范围"],
        [-100, -25, "参数超出-99至99范围"],
        [25, 98, 123],
        [98, 25, 123],
        [-25, -98, -123],
        [-98, -25, -123]
    ],
    ids=["a/b is null",
         "a is null",
         "b is null",
         "a is str",
         "b is str",
         "a/b is normal",
         "b is max",
         "a is max",
         "b is min",
         "a is min",
         "b > max",
         "a > max",
         "b < min",
         "a < min",
         "b is max Boundary",
         "a is max Boundary",
         "b is min Boundary",
         "a is min Boundary"
         ]
)
def number_determine(n):
    if not (isinstance(n, int) or isinstance(n, float)):
        return "参数为非数字"
    elif n > 99 or n < -99:
        return "参数超出-99至99范围"
    return "符合条件"


def number_two(a, b):
    # 测试步骤
    if number_determine(a) == "符合条件":
        if number_determine(b) == "符合条件":
            return a + b
        else:
            return f"[b]{number_determine(b)}"
    else:
        return f"[a]{number_determine(a)}"


def test_number_add(a, b, expected):
    # 测试步骤
    result = number_two(a, b)
    print(result)
    # 断言
    assert result == expected
