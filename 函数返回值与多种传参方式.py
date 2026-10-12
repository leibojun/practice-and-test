def test_return():
    return 1,2,True#返回值不限类型
x,y,z=test_return()#变量与返回值对应接收
print(x,y,z)
#键值对传参
def userinfo(name,age,gender):
    print(f'你的名字是{name},年龄为{age},性别为{gender}')
userinfo(name='xiaoming',age=19,gender='man')
#位置传参
userinfo('xiaoming',20,'man')
#缺省参数，提前设定值
def user2(name,age,gender='男'):#默认参数只能写在最后面
    print(f'你的名字是{name},年龄为{age},性别为{gender}')
user2('xiaoming',20)
#不定长传参
def user3(*args):#输入参数数量随意
    print(args,type(args))
user3('xiaoming',20)#元组形式
def user4(**keywords):
    print(keywords,type(keywords))
user4(name='xiaoming',age=19,gender='man')#输入成对数据，输出为字典形式
