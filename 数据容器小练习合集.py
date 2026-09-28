"""
小练习，给一个字符串“ itheima itcast boxuegu"
统计it出现的次数 并把所有空格替换为|，最后按照|进行字符串切割得到列表 count replace split（分割）
"""
str="itheima itcast boxuegu"
num=str.count("it")
print(f"字符串{str}中有{num}个it字符")
newstr=str.replace(" ","|")
print(newstr)
strlist=newstr.split("|")
print(f"字符串被分割后得到的列表是{strlist}")
