#__str__魔术方法,返回需要输出的字符串，如下
class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Student类对象,name: {self.name},age: {self.age}"
    def __lt__(self,other):
        return self.age < other.age
stu1=student("周杰伦",30)
stu2=student("林俊杰",40)
print(stu1)
print(str(stu1))
#__lt__魔术方法,__le__魔术方法可以比较小于等于，__eq__魔术方法可以比较“相等”情况
print(stu1.age<stu2.age)
print(stu1.age>stu2.age)

