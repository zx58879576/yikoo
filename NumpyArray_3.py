# -*- coding: utf-8 -*-
import numpy as np
def main():
   a = np.arange(12).reshape(3, 4)
   b = np.arange(3)
   c = np.arange(4)
   print("a数组：\n%s"%a)
   print("纵轴插入:\n%s,\n横轴插入：\n%s"%(np.insert(a, 1, b, 1),np.insert(a, 1, c, 0)))#1:纵 0：横
   print("只能在末尾插入：\n%s"%np.append(a, c)) #将值附加到数组的末尾，并返回 1 维数组
   a.resize(4,3)
   print("a数组重设尺寸：\n%s"%a)
   print("a数组左右翻转：\n%s"%np.fliplr(a))
   print("a数组上下翻转：\n%s"%np.flipud(a))
   
   
   """随机数"""
   print("rand:\n%s"%np.random.rand(2, 5))  #指定一个数组，并使用 [0, 1) 区间随机数据填充，这些数据均匀分布。
   print("randn:\n%s"%np.random.randn(1, 10)) #从标准正态分布中返回一个或多个样本值
   print("random_sample:\n%s"%np.random.random_sample([10]))#random_sample(size) 在 [0, 1) 区间内生成指定 size 的随机浮点数。  
   print("randint:\n%s"%np.random.randint(2, 5, 10))#randint(low, high, size, dtype) 生成 [low, high) 的随机整数。
   print("choice:\n%s"%np.random.choice(10, 5))#choice(a, size, replace, p) 给定的数组里随机抽取几个值，类似于随机抽样。
if __name__=="__main__":
    main()
    
 
 
 
 
 
 运行结果：
 a数组：
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
纵轴插入:
[[ 0  0  1  2  3]
 [ 4  1  5  6  7]
 [ 8  2  9 10 11]],
横轴插入：
[[ 0  1  2  3]
 [ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
只能在末尾插入：
[ 0  1  2  3  4  5  6  7  8  9 10 11  0  1  2  3]
a数组重设尺寸：
[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]
a数组左右翻转：
[[ 2  1  0]
 [ 5  4  3]
 [ 8  7  6]
 [11 10  9]]
a数组上下翻转：
[[ 9 10 11]
 [ 6  7  8]
 [ 3  4  5]
 [ 0  1  2]]
rand:
[[0.81384133 0.01758515 0.20516166 0.3479485  0.27987001]
 [0.70425375 0.70532672 0.68154325 0.64920455 0.79970007]]
randn:
[[-0.30878432  0.94104106 -0.41730511  0.8028934   0.38512103  1.2798329
  -1.30370627 -0.00517847  0.00224558 -0.78713787]]
random_sample:
[0.28654134 0.43247126 0.97513813 0.08326514 0.15910308 0.17037561
 0.58830659 0.15617047 0.22102617 0.57621837]
randint:
[2 4 3 4 4 3 4 2 3 2]
choice:
[0 7 8 3 2]
