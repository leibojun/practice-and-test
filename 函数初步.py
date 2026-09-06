#函数是组织好的，可重复使用的用于实现特定功能的代码段   python有很多内置函数比如input
#e.g.写一个len（）函数，统计字符串长度的函数
str1='battlefield'
count=0
for x in str1:#遍历字符串str1
    count+=1
print(count)
#相当于
str1='battlefield'
len=len(str1)
print(len,'（函数方式）')
#或者自定义函数
def my_len(data):
    count=0
    for x in data:
        count+=1
    print(count)
my_len(str1)#这是个函数，定义中的函数本身就包含print
#函数相当于一种算法，或者理解为一种流水线，针对需要多次调用重复代码的情况可以把它封装成函数重复利用

'''
def 函数名称（传入参数）
    函数本体
    return 返回值
'''
#定义后的函数只有在调用时才会工作
def say_hi():#注意这里有一个冒号
    print('hi')
say_hi()#参数和返回值都可以省略
def add(a,b):#函数中定义的参数为形式参数，作用是明确运算方式
    result = a+b
    print(f'{a}+{b}的结果是{result}')
add(1,2)#调用函数时传入的为实际参
#函数的返回值
def add(a,b):
    result = a+b
    return result#赋值阶段，不会打印出来，但会把add(a,b)这个值返回出来以供调用，函数的返回值可以用变量去接收
#return 之后相当于函数结束，后面的函数代码均不会执行
r=add(1,2)
print(r)
#对于无返回值的函数，返回值为None,用变量去接收没什么用，可能只是普通的打印函数
#判断上，None相当于false
#功能上，none可以用于声明无初始内容的变量


#函数的嵌套调用
def func_a():
    print('1 ',end='')
def func_b():
    print('2 ',end='')
    func_a()#先运行完这个函数，再继续进行func_b函数
    print('3')
func_b()


#函数的变量作用域
#局部变量和全局变量，局部变量在函数运行完即销毁，无法在外部调用
#在函数内部可以局部地去修改全局变量
#global关键字可以在函数中修改全局变量
num=200#此时定义的为全局变量
def demo_a():
    global num#此步修改了全局变量
    num=400#此步修改了全局变量
    print(num)
demo_a()
print(num)



