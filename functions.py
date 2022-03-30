def reciprocal(value):
    value = round(float(1) / (float(value)), 10)
    return value


# 计算阶乘
def factorial(value):
    sum = 1
    if value == 0 or value == 1:
        sum = 1
    for i in range(value):
        sum += sum * i
    return sum

# 计算sin
# def sin(x):
#     e = 10^(-15)
#     sum = 0
#     evl = x
#     n = 1
#     while(abs(evl)>e):
#         sum = sum+evl
#         a = (-1)**n
#         b = evl**(2*n+1)
#         c = factorial((2*n+1))
#         evl = a*b/c
#         n +=1
#
# print(sin(1))


# 计算sin
# class cc:
#     def arctan(float, str):
#         # 输入判断
#         if(float >= -65535 and float <= 65536):
#             compute = True
#         else:
#             compute = False
#     # 符合输入规范则进行计算，并返回结果；否则返回"None"
#         if(compute):
#             # 反正切计算
#             ret = 0
#             get = float
#             index = 1
#             n = 0
#             while index < 10000:
#                 index = index + 1
#                 ret = ret+(((-1)**n)/(2*n+1))*(get**(2*n+1))
#                 n = n + 1
#             ret = "%.3f" % ret
#             if (str == "角度"):
#                 ret = ret / 57.3
#         else:
#             ret = "None"
#         return ret
def arcsine(float, str):
    # 输入正确性判断
    if(float >= -1 and float <= 1 and str == "弧度"):
        compute = True
    elif(float >= -1 and float <= 1 and str == "角度"):
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
        if(str == "弧度"):  # 结果输出采用弧度制
            while index < 197293:
                index = index + 2
                res = res + i*(float**index/index)
                m = m + 2
                n = n + 2
                i = i * n/m
            res = "%.2f" % res
        else:             # 结果输出采用角度制
            while index < 961337:
                index = index + 2
                res = res + i*(float**index/index)
                m = m + 2
                n = n + 2
                i = i * n/m
            res = res / 3.14 * 180
            res = "%.2f" % res
        #
    else:
        res = "None"
    return res


def mycos(x, e=1e-3):
    item = 1
    sum = 0
    i = 0
    f = 1
    while abs(item) > e:
        item = f * ((x**i) / fact(i))
        sum += item
        f = -f
        i += 2

    return sum


def fact(n):
    result = 1
    for i in range(1, n+1):
        result *= i

    return result


class MyCos(object):
    def __init__(self, e=1e-3):
        self.e = e

    def mycos(self, x):
        item = 1
        sum = 0
        i = 0
        f = 1
        while abs(item) > self.e:
            item = f * ((x**i) / fact(i))
            sum += item
            f = -f
            i += 2

        return sum

    def fact(self, n):
        result = 1
        for i in range(1, n+1):
            result *= i

        return result


def sin_t(x):
    # pi = 3.14159265
    return round(math.sin(x*pi/180), 10)
    # ss = cc()
    # x = int(x)
    # ss = int(ss)
    # mm=ss.arctan()
    # return round(ss.arctan(x), 10)


# 计算cos
def cos_t(x):
    pi = 3.14159265
    cos = MyCos()
    # 输入待计算数值
    return round(cos.mycos(x*pi/180), 10)


# 计算tan
def tan_t(x):
    return round(arcsine(x, "角度"), 10)


# 计算csc
def csc_t(x):
    return round(float(1)/math.sin(x), 10)


# 计算sec
def sec_t(x):
    return round(float(1)/math.cos(x), 10)


# 计算lg
def lg_t(x):
    return round(math.log10(x), 10)

# 计算ln


def ln_t(x):
    return round(math.log(x, math.e), 10)
