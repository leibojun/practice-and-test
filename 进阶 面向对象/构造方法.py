class Student:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        print("Student类创建了一个对象")
stu1=Student("周杰伦","M",31)
print(stu1.name)
print(stu1.gender)