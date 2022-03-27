"""
Function: compute the arcsine of a number
Author: JavaCat0513
Time: 2022/3/27 17:36
Version: 3.0
"""

def arcsine(float,str):
    # 输入正确性判断
    if(float >= -1 and float <= 1 and str == "弧度"):
        compute = True
    elif(float >= -57.3 and float <= 57.3 and str == "角度"):
        float = float / 57.3
        compute = True
    else:
        compute = False
    #
    # 符合输入规范则进行计算，并返回结果；否则返回"None"
    if(compute):
        # 反正弦计算
        res = float
        index = 1
        m = 2
        n = 1
        i = 1/2
        while index < 197293:
            index = index + 2
            res = res + i*(float**index/index)
            m = m + 2
            n = n + 2
            i = i * n/m
        res = "%.2f" % res
        #
    else:
        res = "None"
    return res
    #

    # 精度确定
    # accuracy = 0.001
    # arcsinx = 1.00
    # index = 1
    # m = 2
    # n = 1
    # i = 1/2
    # res = 0
    # keep_computing = True
    # while keep_computing:
    #     res = 3.14/2 - arcsinx
    #     if(res < accuracy):
    #         keep_computing = False
    #     else:
    #         index = index + 2
    #         arcsinx = arcsinx + i*(1/index)
    #         m = m + 2
    #         n = n + 2
    #         i = i * n/m
    # print(index)#197293-0.001-3.14
    #