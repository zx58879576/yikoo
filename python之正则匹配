
# -*- coding: utf-8 -*-
"""re 模块  ,匹配 match 和search"""
import re
def main():
    str1="baidu" 
    str2="baidu.com"
    str3="WWW.BAIDU.COM"
    print("从头开始匹配：%s"%re.match(str1,str2))
    print("从任意位置开始匹配：%s"%re.search(str1,str3,re.I)) # re.I 忽略大小写,
   
    str4=input("请输入生日：(格式：xxxx-xx-xx)")
    pattern1="[0-9]{4}-[0-9]{2}-[0-9]{2}"
    if re.match(pattern1,str4,re.I):
         print("格式正确")
    else:
         print("格式错误")
       
    str5=input("请输入电话号码：")
    pattern2="^((\d{3,4})|(\(\d{3,4}\)-))?\d{7,8}$"
    ''' \d表示数字，{3,4}表示3到4位数 , ? 表示可有可无 ， \(表示（
         ^ 表示开始边界   $ 表示结束边界     
    '''
    if re.match(pattern2,str5,re.I):
         print("电话号码正确")
    else:
         print("电话号码错误")
      
    
    str6=input("请输入邮箱：")
    pattern3=r"""
              [0-9a-zA-Z]    #匹配第一个字母，由非数字组成   
              \w+@\w+       #用户名中间部分由字母 数字 下划线组成   
              \.            #匹配出现的·，必须转义
              (cn|com|com.cn|net|gov)   #匹配邮箱域名，只允许指定的几个
                """
    if re.match(pattern3,str6,re.I|re.X):  #re.X忽略正则表达式中空白和注释
         print("邮箱格式正确")
    else:
         print("邮箱格式错误")
        
        
    str7="d23did:123,rrid:333,j :baidu 1992-09-21,ee"
    pattern4=r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"
    #(\d{4}) 其中（）表示分组  ?P<year>设置分组名称
    match=re.search(pattern4,str7)
    print("获取所有分组数据：%s"%match.group())
    print("获取'year'组数据：%s"%match.group(1))
    print("获取'month'组数据：%s"%match.group("month")) #可通过名称获取，也可通过索引
    print("获取'day'组数据：%s"%match.group(3))
   
    pattern5=r"(?=b)(?P<name>\w+)"  #匹配b开头的
    print(re.findall(pattern5,str7))
   
    pattern6=r"(?<=id:)(?P<name>\w+)"   #匹配id:数据
    print(re.findall(pattern6,str7))  
if __name__=="__main__":
    main()
    
    
    

    
    





运行结果：
获取所有分组数据：1992-09-21
获取'year'组数据：1992
获取'month'组数据：09
获取'day'组数据：21
['baidu']
['123', '333']

runfile('D:/pythonWork/ecjtu/main.py', wdir='D:/pythonWork/ecjtu')
从头开始匹配：<re.Match object; span=(0, 5), match='baidu'>
从任意位置开始匹配：<re.Match object; span=(4, 9), match='BAIDU'>

请输入生日：(格式：xxxx-xx-xx)1994-02-21
格式正确

请输入电话号码：(023)-23141231
电话号码正确

请输入邮箱：ewdq33@dd.com
邮箱格式正确
获取所有分组数据：1992-09-21
获取'year'组数据：1992
获取'month'组数据：09
获取'day'组数据：21
['baidu']
['123', '333']
