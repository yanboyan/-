# -*- coding:utf-8 -*-
# ICT Python 三期一阶段
# @Time : 2023/4/25 21:53
# @Author : byyan
# @File : school_assignment_day1.py
# @Software: PyCharm
def num_two(a,b):
    if isinstance(a,int) != True and isinstance(b,int) != True:
        print(f"参数不为-99到99的整数或浮点数")
    elif isinstance(a,float) != True and isinstance(b,float) != True:
        print(f"参数不为-99到99的整数或浮点数")
    elif  -99 <= a <= 99 and -99 <= b <= 99:
        c = a + b
        print(f"a和b相加为：{c}")
    else:
        print(f"参数不为-99到99的整数或浮点数")
if __name__ == '__main__':
    num_two("a",2)