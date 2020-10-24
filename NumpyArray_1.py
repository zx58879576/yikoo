# -*- coding: utf-8 -*-
import numpy as np

"""三角函数"""
def main():
    a=np.random.rand(5)
    b=np.random.rand(6)
    print(np.rad2deg(np.pi*2)) #弧度转换为度
    print(np.degrees(np.pi))   #弧度转换为度
    print(np.deg2rad(90))      #度转换为弧度
    print(np.radians(90))      #度转换为弧度
    print(np.hypot(3,4))       #直角三角形求斜边
    print(np.arctan(0.5))      #三角反正切
    print(np.arccos(0.5))      #三角反余弦
    print(np.arcsin(0.5))      #三角反正弦
    print(np.tan(np.pi*0.25))      #三角正切
    print(np.cos(np.pi*0.5))      #三角余弦
    print(np.sin(np.pi*0.5))      #三角正弦
    
    """数值修约"""
    number = np.random.randn(5)
    print("number:%s"%number)
    print("around:\n%s"%np.around(a))        #平均到给定的小数位数
    print("rint:\n%s"%np.rint(a))          #修约到最接近的整数
    print("fix:\n%s"%np.fix(a))           #向 0 舍入到最接近的整数
    print("round_:\n%s"%np.round_(a))        #将数组舍入到给定的小数位数
    print("floor:\n%s"%np.floor(a))         #返回输入的底部(标量 x 的底部是最大的整数 i)
    print("ceil:\n%s"%np.ceil(a))          #返回输入的上限(标量 x 的底部是最小的整数 i)
    print("trunc:\n%s"%np.trunc(a))         #返回输入的截断值

    
if __name__=="__main__":
    main()
    
    
    
   
   
  
 运行结果：
 360.0
180.0
1.5707963267948966
1.5707963267948966
5.0
0.4636476090008061
1.0471975511965979
0.5235987755982989
0.9999999999999999
6.123233995736766e-17
1.0
number:[-0.54003954 -1.30214158  0.67323441 -1.28141703  1.0773701 ]
around:
[1. 0. 0. 1. 0.]
rint:
[1. 0. 0. 1. 0.]
fix:
[0. 0. 0. 0. 0.]
round_:
[1. 0. 0. 1. 0.]
floor:
[0. 0. 0. 0. 0.]
ceil:
[1. 1. 1. 1. 1.]
trunc:
[0. 0. 0. 0. 0.]
