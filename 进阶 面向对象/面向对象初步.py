#设计类 创建对象 对象属性赋值  类似于C语言中结构体
#设计类
class Student:
    name = None
    gender = None
    nationality = None
    native_place = None
    age = None
    def say_hi(self):#类中可以记录行为，定义在类内部的函数叫做方法   传参位置必须填上self
        print("Hello, my name is " + self.name)
    def say_hi2(self,msg):
        print(f"Hello, my name is {self.name},{msg}")

#创建对象
stu1 = Student()#既是变量，也是对象
stu1.name = "林俊杰"
stu1.gender = "M"
stu1.nationality = "China"
stu1.native_place = "Shandong"
stu1.age = 31
print(stu1.name)
#使用类中定义的方法
Student.say_hi(stu1)#self形参的位置放入新定义的变量stu1
stu1.say_hi()#方法引用法2,与上一行输出一致
stu1.say_hi2("诶哟不错哟")#此时传入到msg处