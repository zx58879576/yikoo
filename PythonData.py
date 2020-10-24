# -*- coding: utf-8 -*-
""" set集合"""
def main():
      set_a=set("abcd")
      set_b=set("cdef")
      set_c=set(["hello","hello","hel"  ,"baidu","baidu"])
      set_c.add("com")
      print(set_c)     #去除重复元素
      print("【并集运算】 %s,%s"%(set_a.union(set_b),set_a|set_b))
      print("【差集运算】 %s,%s"%(set_a.difference(set_b),set_a-set_b))
      print("【交集运算】 %s,%s"%(set_a.intersection(set_b),set_a&set_b))
      print("【对称差集】 %s,%s"%(set_a.symmetric_difference(set_b),set_a^set_b))
if __name__=="__main__":
    main()
    
    


"""双端队列"""
from collections import deque   #collections模块中deque操作
def main():
    info_deque=deque(("abc","可乐翔"))
    info_deque.append("ddd")    #队列后端加数据
    info_deque.appendleft("ffff")  #队列前端加数据
    info_deque.reverse()
    print("队列反转后：%s"%info_deque)
    print("队列中'abc'元素个数:%s"%info_deque.count("abc"))
    info_deque.remove('ffff')    #移除指定元素
    print("删除ffff后队列:%s"%info_deque)
    print("弹出数据：%s"%info_deque.pop())  #队列前端弹出
    print("弹出数据：%s"%info_deque.popleft())  #队列后端弹出
    print("弹出数据：%s"%info_deque.pop())
    info_deque.clear()   #清空队列
if __name__=="__main__":
    main()   



"""堆"""
import heapq
def main():
    data=[3,6,2,8,5,4,7]
    print("原始data列表：%s"%data)
    heapq.heapify( data )   #根据列表data创建堆（小顶堆）
    heapq.heappush(data,0)  #建好堆后加入元素0成新堆
    print("创建堆后：%s"%data)
    print("弹出最小元素：%s后的堆为：%s"%(heapq.heappop(data),data))
    print("最小前三个元素：%s"%heapq.nsmallest(3,data))
    print("弹出最小元素%s并加入元素4后的堆为：%s"%(heapq.heapreplace(data,4),data))#弹出最小元素并加入新元素
    print("最大前2个元素：%s"%heapq.nlargest(2,data))
if __name__=="__main__":
    main()
    

"""枚举"""
import enum
@enum.unique  #限定枚举对象值唯一
class Color(enum.Enum): #必须强制继承父类
   RED=0
   BLUE=1
   GREEN=2
def main():
   color=Color.BLUE
   print("枚举对象：%s,值为%s"%(color.name,color.value))
if __name__=="__main__":
    main()
    
    


运行结果：
{'baidu', 'hello', 'com', 'hel'}
【并集运算】 {'f', 'a', 'c', 'e', 'd', 'b'},{'f', 'a', 'c', 'e', 'd', 'b'}
【差集运算】 {'b', 'a'},{'b', 'a'}
【交集运算】 {'d', 'c'},{'d', 'c'}
【对称差集】 {'f', 'a', 'e', 'b'},{'f', 'a', 'e', 'b'}
队列反转后：deque(['ddd', '可乐翔', 'abc', 'ffff'])
队列中'abc'元素个数:1
删除ffff后队列:deque(['ddd', '可乐翔', 'abc'])
弹出数据：abc
弹出数据：ddd
弹出数据：可乐翔
原始data列表：[3, 6, 2, 8, 5, 4, 7]
创建堆后：[0, 2, 3, 5, 6, 4, 7, 8]
弹出最小元素：0后的堆为：[2, 5, 3, 8, 6, 4, 7]
最小前三个元素：[2, 3, 4]
弹出最小元素2并加入元素4后的堆为：[3, 5, 4, 8, 6, 4, 7]
最大前2个元素：[8, 7]
枚举对象：BLUE,值为1
