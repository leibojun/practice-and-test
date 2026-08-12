age=int(input("请输入您的年龄："))# 注意input默认接受字符串，想让age为数字型需要进行类型转换
# if else 语句
if age>=18:
    print("you are adult,ten yuan more please.")
else:
    print("you are a kid,play for free")
print("welcome and have a nice day")
#if elif 多条件语句
age=int(input("please enter your age"))
if age<=18:
    print("you are a kid,play for free")
elif age>=18and age<65:
    print("you are a adult,tenyuan more please.")
else:
    print("the elder is for free")
print("welcome and have a nice day")