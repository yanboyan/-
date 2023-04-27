# -*- coding:utf-8 -*-
# pytest day2
# @Time : 2023/4/26 23:05
# @Author : Augustine
# @File : test_school_assignment_day2.py
# @Software: PyCharm
import null as null
import pytest

# 在调用每个测试函数之前打印【开始计算】在调用测试函数之后打印【结束计算】
# 调用完所有的测试用例最终输出【结束测试】

def setup_function():
    print("开始计算")

def teardown_function():
    print("结束计算")

def teardown_module():
    print("结束测试")

def number_determine(n):
    # 条件判断
    if not (isinstance(n, int) or isinstance(n, float)):
        return "参数为非数字"
    elif n > 99 or n < -99:
        return "参数超出-99至99范围"
    return "符合条件"


def number_two(a, b):
    # 相加
    if number_determine(a) == "符合条件":
        if number_determine(b) == "符合条件":
            return a + b
        else:
            return f"[b]{number_determine(b)}"
    else:
        return f"[a]{number_determine(a)}"

@pytest.mark.parametrize(
    "a,b,expected",
    [
        [null, null, "[a]参数为非数字"],
        [null, 25, "[a]参数为非数字"],
        [25, null, "[b]参数为非数字"],
        ["m", 25, "[a]参数为非数字"],
        [25, "m", "[b]参数为非数字"],
        [25, 25, 50],
        [25, 99, 124],
        [99, 25, 124],
        [-25, -99, -124],
        [-99, -25, -124],
        [25, 100, "[b]参数超出-99至99范围"],
        [100, 25, "[a]参数超出-99至99范围"],
        [-25, -100, "[b]参数超出-99至99范围"],
        [-100, -25, "[a]参数超出-99至99范围"],
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

def test_number_add(a, b, expected):
    # 测试步骤
    result = number_two(a, b)
    print(result)
    # 断言
    assert result == expected
