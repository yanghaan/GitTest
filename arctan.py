def arctanx():
   tanx=float(input("请输入正切值："))
    # 输入判断
   if(tanx >= -65535 and tanx <= 65535 ):
        compute = True
   else:
        compute = False
    # 符合输入规范则进行计算，并返回结果；否则返回"None"
   if(compute):
        # 反正切计算
        ret = 0
        get = tanx
        index = 1
        n = 0
        while index < 100000:
            index = index + 1
            ret = ret+(((-1)**n)/(2*n+1))*(get**(2*n+1))
            n = n + 1
        ret = "%.3f" % ret
        print(tanx,"对应的反正切值arctanx为：",ret)
   else:
         ret = "None"
   return ret
