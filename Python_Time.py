# -*- coding: utf-8 -*-
"""time calendar  datetime 模块"""
import time
import calendar
import datetime
def main():
   time1=time.time()  #获取当前时间戳
   time2=time.localtime(time1) #localtime()时间戳转为时间元组
   print("当前时间戳：%s"%time1)
   print("当前时间：%s"%time.asctime())
   print("时间戳转时间元组：%s"%str(time2))
   time3=(2018,4,12,22,12,12,4,23,0)  #自定义时间元组
   print("时间元组转时间戳：%s"%time.mktime(time3))
   print("时间元组转格式化：%s"%time.strftime("%Y-%m-%d %H:%M:%S",time3))
   print("获取时间元组中的日期数据：%s"%time.strftime("%F",time3))
   print("获取时间元组中的时间数据：%s"%time.strftime("%T",time.localtime(time.time())))
   print("**************************************")
   
   
   cal=calendar.month(2020,10)  #显示月历
   print(cal)
   cal_1=calendar.calendar(2020)  #显示年历，年历有很多设置参数
   print(cal_1)
   
   
   time4=datetime.date.today()   #今天日期
   time5=datetime.time(21,13,23,42)
   print(time4)
   print("返回星期数：%s"%time4.weekday())
   print("格式化日期显示：%s"%time4.isoformat())
   print("时：%s,分：%s,秒：%s，微秒：%s"%(time5.hour,time5.minute,time5.second,time5.microsecond))
   
   
   
   time6=datetime.datetime(2020,12,12,11,34,45)
   print("当前时间：%s"%str(time6))
   print("34小时后时间:%s"%str(time6+datetime.timedelta(hours=34)))
   print("10天前时间:%s"%str(time6+datetime.timedelta(days=-10)))

if __name__=="__main__":
    main()
    
    

运行结果：
当前时间戳：1602251230.1592486
当前时间：Fri Oct  9 21:47:10 2020
时间戳转时间元组：time.struct_time(tm_year=2020, tm_mon=10, tm_mday=9, tm_hour=21, tm_min=47, tm_sec=10, tm_wday=4, tm_yday=283, tm_isdst=0)
时间元组转时间戳：1523542332.0
时间元组转格式化：2018-04-12 22:12:12
获取时间元组中的日期数据：2018-04-12
获取时间元组中的时间数据：21:47:10
**************************************
    October 2020
Mo Tu We Th Fr Sa Su
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30 31

                                  2020

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
       1  2  3  4  5                      1  2                         1
 6  7  8  9 10 11 12       3  4  5  6  7  8  9       2  3  4  5  6  7  8
13 14 15 16 17 18 19      10 11 12 13 14 15 16       9 10 11 12 13 14 15
20 21 22 23 24 25 26      17 18 19 20 21 22 23      16 17 18 19 20 21 22
27 28 29 30 31            24 25 26 27 28 29         23 24 25 26 27 28 29
                                                    30 31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
       1  2  3  4  5                   1  2  3       1  2  3  4  5  6  7
 6  7  8  9 10 11 12       4  5  6  7  8  9 10       8  9 10 11 12 13 14
13 14 15 16 17 18 19      11 12 13 14 15 16 17      15 16 17 18 19 20 21
20 21 22 23 24 25 26      18 19 20 21 22 23 24      22 23 24 25 26 27 28
27 28 29 30               25 26 27 28 29 30 31      29 30

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
       1  2  3  4  5                      1  2          1  2  3  4  5  6
 6  7  8  9 10 11 12       3  4  5  6  7  8  9       7  8  9 10 11 12 13
13 14 15 16 17 18 19      10 11 12 13 14 15 16      14 15 16 17 18 19 20
20 21 22 23 24 25 26      17 18 19 20 21 22 23      21 22 23 24 25 26 27
27 28 29 30 31            24 25 26 27 28 29 30      28 29 30
                          31

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
          1  2  3  4                         1          1  2  3  4  5  6
 5  6  7  8  9 10 11       2  3  4  5  6  7  8       7  8  9 10 11 12 13
12 13 14 15 16 17 18       9 10 11 12 13 14 15      14 15 16 17 18 19 20
19 20 21 22 23 24 25      16 17 18 19 20 21 22      21 22 23 24 25 26 27
26 27 28 29 30 31         23 24 25 26 27 28 29      28 29 30 31
                          30

2020-10-09
返回星期数：4
格式化日期显示：2020-10-09
时：21,分：13,秒：23，微秒：42
当前时间：2020-12-12 11:34:45
34小时后时间:2020-12-13 21:34:45
10天前时间:2020-12-02 11:34:45
