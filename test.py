print("战地风云，解放峰")
# 规范要求，井号和注释内容中间空一格
"""
中间为多行注释，格式为三个引号，上下都有
"""
# 定义变量，变量的作用是记录数据,存储数据
a=1
print("a的值为：",a)# 会输出1,用逗号隔开
b=a-10
print(b)# 会输出-9
print(type(a))# type用于查看变量类型
print(type(111.3))
print(type("nmsl"))
#数据类型转换
num=str(11)#str()/int()都具有返回值，可用print打印或者使用一个变量来接收
print(type(num),num)# 输出结果为<class 'str'> 11
name='\'battlefield'# \可用于取消引号的功能，将其转化为单纯的字符
print(name)
# 字符串拼接
print('kale'+'dianjing'+name)#字符串可直接用加号拼接
#字符串和数字类型拼接
a=40
b=50
str1='我的显卡是%d %d'%(a,b)#整数用%d，浮点数用%f，字符串用%s,占位符在变量部分就要写入
print(str1)
# %m.nf可用于控制数字的宽度和精度,m为宽度,n为精度
num=13.345
print("%7.2f"%num)
# 快速格式化字符串，快捷占位法print(f"balabala{xxxxx}")
a=1111
b=2222
print(f"the number is {a}")# 这个f很关键，但是这个占位方法无法做精度控制，不过他不限变量类型
# 表达式：有明确执行结果的代码语句 eg. 1+1   name=“张三” 它可以直接格式化占位
print("2*2的运算结果是%d"%(2*2))# 普通格式化
print(f"2*2的结果是{2*2}")# 快速格式化
# 平方运算符 **
print(f"2的三次方等于{2**3}")
# input()语句,类似c语言中的scanf，默认接受类型都是字符串，需要其他种类需要进行类型转换
name=input("请告诉我你是谁")#input后面括号相当于print语句，作用是提示输入信息
print("我的名字是：%s"%name)
num=input("你几岁")# 默认接受类型都是字符串，需要其他种类需要进行类型转换
num=int(num)# 注意类型转化的语法
print("你的年龄是%d"%num)
# 黑马第三阶段
# 布尔类型，判断式返回值为布尔类型
bool_1=True
bool_2=False
print(f"布尔1变量的内容是{bool_1}类型是{type(bool_1)}")# 输出结果为    布尔1变量的内容是True类型是<class 'bool'>
a=10
b=15
print(a==b)# 输出值为false，输出类型为布尔型
print(a<b)# 输出值为true
print(a+b)# 输出结果为25
# 输入不换行操作
print("hello world",end='')
print("   hello my friend")
# 输入对齐操作
print("hello\tfriend")
print("nice\tmeet ")
