# -*- coding: utf-8 -*-
import numpy as np
def main():
   a=np.array([[1,4],[2,5]])  #通过列表创建数组
   b=np.array([(1,2),(4,6),(2,12)])#通过列表元组创建数组
   c=np.arange(1,12,1.5,dtype='float64') #arange() 的功能是在给定区间内创建一系列均匀间隔的值
   d=np.arange(4).reshape(2,2) #生成2*2数组
   e=np.linspace(0,12,6,endpoint=False)#linspace 用于在指定的区间内返回间隔均匀的值
   f=np.ones((2,3)) #numpy.ones 用于快速创建数值全部为 1 的多维数组
   g=np.zeros((2,4),dtype="int64",order='C') #填充为 0
   h=np.eye(5,5,0,dtype='float32')#numpy.eye 用于创建一个二维数组，其特点是k 对角线上的值为 1
   print("a数组：\n%s"%a)
   print("转置:%s,元素数：%s\n单元素字节数：%s，总元素字节数%s"%(np.transpose(a),a.size,a.itemsize,a.nbytes))#转置也可a.T
   print("维度：%s，形状：%s,每个维度字节数组：%s"%(a.ndim,a.shape,a.strides))
   print("b数组：\n%s"%b)
   print("重塑形状：\n%s,\n数组一维化：%s"%(b.reshape(2,3),np.ravel(b,order='C')))
   print("轴移动：\n%s,\n轴交换：\n%s"%(np.moveaxis(b,0,-1),np.swapaxes(b,0,-1)))
   print("c数组：\n%s"%c)
   print("d数组：\n%s"%d)
   print("a、b数组纵轴连接:\n%s，\na、d横轴连接:\n%s"%(np.concatenate((a,b),axis=0),np.concatenate((a,d),axis=1)))
   print("e数组：\n%s"%e)
   print("e数组拆分：\n%s,\nd数组拆除部分：\n%s"%((np.split(e,3)),np.delete(d,1,1)))
   print("f数组：\n%s"%f)
   print("g数组：\n%s"%g)
   print("h数组：\n%s"%h)
if __name__=="__main__":
    main()
    
    

运行结果：
a数组：
[[1 4]
 [2 5]]
转置:[[1 2]
 [4 5]],元素数：4
单元素字节数：4，总元素字节数16
维度：2，形状：(2, 2),每个维度字节数组：(8, 4)
b数组：
[[ 1  2]
 [ 4  6]
 [ 2 12]]
重塑形状：
[[ 1  2  4]
 [ 6  2 12]],
数组一维化：[ 1  2  4  6  2 12]
轴移动：
[[ 1  4  2]
 [ 2  6 12]],
轴交换：
[[ 1  4  2]
 [ 2  6 12]]
c数组：
[ 1.   2.5  4.   5.5  7.   8.5 10.  11.5]
d数组：
[[0 1]
 [2 3]]
a、b数组纵轴连接:
[[ 1  4]
 [ 2  5]
 [ 1  2]
 [ 4  6]
 [ 2 12]]，
a、d横轴连接:
[[1 4 0 1]
 [2 5 2 3]]
e数组：
[ 0.  2.  4.  6.  8. 10.]
e数组拆分：
[array([0., 2.]), array([4., 6.]), array([ 8., 10.])],
d数组拆除部分：
[[0]
 [2]]
f数组：
[[1. 1. 1.]
 [1. 1. 1.]]
g数组：
[[0 0 0 0]
 [0 0 0 0]]
h数组：
[[1. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0.]
 [0. 0. 1. 0. 0.]
 [0. 0. 0. 1. 0.]
 [0. 0. 0. 0. 1.]]
