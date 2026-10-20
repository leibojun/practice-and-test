#模块就是一个工具包，里面有类/函数/变量等
#基本语法   [from 模块名] import [模块/类/变量/函数/*星号表示导入全部内容][as 别名]
#用法一
import time
print("hello")
time.sleep(2)#.表示层级关系 模块.功能
print("hello No2")
#用法二
from time import sleep#from 模块名 import 功能名       针对使用某一种功能
print("hello No3")
sleep(2)#直接用了功能名字
print("hello No4")
#用法三
from time import *#引入了全部功能
print("hello No5")
sleep(2)
print("hello No6")
#改名效果
from time import sleep as 睡觉
print("hello No7")
睡觉(2)
print("hello No8")