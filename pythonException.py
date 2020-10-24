# -*- coding: utf-8 -*-
""" 异常统一处理 &&多异常处理"""
import traceback    #traceback模块获取异常完整信息
def main():
      try:
        print("程序开始")
        num1=int(input("输入一个数："))
        num2=int(input("再输入一个数："))
        result=num1/num2
        print(result)
      except ZeroDivisionError as err:
        print("出现异常%s"%traceback.format_exc())#获取异常完整信息
      except Exception as err:   #异常统一处理
          print("出现异常：%s"%err)
     
      else:
        print("程序无异常")
      finally:
        print("无论是否异常，都会执行我")
      print("程序完成")
if __name__=="__main__":
    main()
 
    
def fun():
    try:
        raise NameError("抛出名字异常") #raise抛出异常
    except Exception as err:
        print("出现异常%s"%err)
        raise TypeError("类型异常")from err
def main():
    try:
        fun()
    except Exception as err:
        print("出现异常%s,cause=%s"%(err,err.__cause__)) #err.__cause__异常原因，对应from
if __name__=="__main__":
    main()


运行结果：
程序开始

输入一个数：5

再输入一个数：0
出现异常Traceback (most recent call last):
  File "D:\pythonWork\ecjtu\main.py", line 9, in main
    result=num1/num2
ZeroDivisionError: division by zero

无论是否异常，都会执行我
程序完成
出现异常抛出名字异常
出现异常类型异常,cause=抛出名字异常
