#异常捕获
try:open("D:/aaa.txt","r",encoding="utf-8")
except:
    print("error in last code")
#捕获特定异常
try:
    print(name)
except NameError as e:
    print("出现了未定义的变量")
    print(e)
try:
    a=1/0
except ZeroDivisionError as b:
    print("0作除数")
    print(b)
#全能异常捕获Exception
try:
    print(name)
except Exception as e:
    print(e)
#异常的finally 有无异常都需要执行的一段代码
try:
    print("name")
except Exception as e:
    print(e)
else:#无异常则在try后运行else（如果有的话）
    print("corret")
finally:
    print("finally最终都要执行，不管有没有bug")