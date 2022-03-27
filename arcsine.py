"""
Function: compute the arcsine of a number
Author: JavaCat0513
Time: 2022/3/27 9:28
Version: 1.0
"""

# 欢迎语句
print("欢迎！您可以在这里计算得到一个数的反正弦值,结果将为您保留两位小数~")
#
# 输入正确性判断
keep_asking = True
while keep_asking:
    try:
        print("请输入您想计算的数字(-1~1): ")
        x = input()
        x = float(x)
        if(x >= -1 and x <= 1):
            keep_asking = False
        else:
            print("抱歉，您只能输入(-1~1)范围内的数字！请重新输入~")
    except ValueError:#异常处理
        print("抱歉，您输入的文本只能是阿拉伯数字！请重新输入~")
#
# 反正弦计算
arcsinx = x
index = 1
m = 2
n = 1
i = 1/2
while index < 197293:
    index = index + 2
    arcsinx = arcsinx + i*(x**index/index)
    m = m + 2
    n = n + 2
    i = i * n/m
print(x,"的反正弦值为%.2f" % arcsinx)
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