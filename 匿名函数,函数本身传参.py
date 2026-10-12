#函数中可以调用其他函数,函数作为参数传入其他函数中
def test(compute):
    result=compute(1,2)#本质上是一种对逻辑运算的传递，而非数据的传递
    print(result,type(result),type(compute))
def compute(x,y):
    return x+y
test(compute)
#lambda关键字，定义一个一次性的无名函数
def test2(compute):
    result=compute(1,2)
    print(result)
test2(lambda x,y:x-y)#lambda关键字使用方法，只表示一次运算逻辑，只能写一行

