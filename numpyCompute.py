# -*- coding: utf-8 -*-
import numpy as np

"""求和、求积、差分"""
def main():
    a=np.arange(1,13).reshape(3,4)
    print("a数组：\n%s"%a)
    print("指定轴上的数组元素的乘积:\n%s"%np.prod(a,1))
    print("指定轴上的数组元素的总和:\n%s"%np.sum(a,1))
    print("指定轴上的数组元素的乘积:\n%s"%np.nanprod(a,0)) #0：纵轴 1：横轴
    print("指定轴上的数组元素的总和:\n%s"%np.nansum(a,0))
    print("沿给定轴的元素的累积乘积:\n%s"%np.cumprod(a,1))
    print("沿给定轴的元素的累积总和:\n%s"%np.cumprod(a,1))
    print("沿指定轴的第 n 个离散差分:\n%s"%np.diff(a,3,1))
    print("数组的连续元素之间的差异:\n%s"%np.ediff1d(a,3,1))
    print(" N 维数组的梯度:\n%s"%np.gradient(a))

    """指数和对数"""
    b=np.arange(1,5).reshape(2,2)
    print("^^^^^^^^^^^^^^^^^^^^^^^")
    print("a数组：\n%s"%b)
    print(" 输入数组中所有元素的指数:\n%s"%np.exp(b))
    print(" 计算自然对数:\n%s"%np.log(b))
    print(" 计算常用对数:\n%s"%np.log10(b))
    print(" 计算二进制对数:\n%s"%np.log2(b))
    
    
    """算术运算"""
    c=np.arange(5,9).reshape(2,2)
    print("^^^^^^^^^^^^^^^^^^^^^^^")
    print("a数组：\n%s"%c)
    print(" 对应元素相加:\n%s"%np.add(b,c))
    print(" 求倒数 1/x:\n%s"%np.reciprocal(c))
    print(" 对应负数:\n%s"%np.negative(c))
    print(" 求解乘法:\n%s"%np.multiply(b,c))
    print(" 相除 x1/x2:\n%s"%np.divide(b,c))
    print("  x1^x2:\n%s"%np.power(c,b))
    print(" 减法:\n%s"%np.subtract(c,b))
    print(" 除法的元素余项:\n%s"%np.fmod(c,b))
    print(" 余项:\n%s"%np.mod(c,b))
    print(" 除法余数:\n%s"%np.remainder(c,b))
    
    
    """矩阵和向量积"""
    print("^^^^^^^^^^^^^^^^^^^^^^^")
    num1=np.matrix([[1,2,3],[4,5,6]])
    num2=np.matrix([[2,3],[4,5],[1,2]])
    d=np.arange(9).reshape(3,3)
    print(" 两个数组的矩阵乘积:\n%s"%np.matmul(num1,num2))
    print(" 两个数组的点积:\n%s"%np.dot(num1,num2))
    print(" 两个向量的点积:\n%s"%np.vdot([1,3,4],[2,3,4]))
    print(" 两个数组的内积:\n%s"%np.inner([1,3,4],[2,3,4]))
    print(" 两个向量的外积:\n%s"%np.outer(num1,num2))
    print(" 两个向量的外积:\n%s"%np.outer(num1,num2))
    
if __name__=="__main__":
    main()