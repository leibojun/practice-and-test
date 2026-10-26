class Student():
    def __init__(self,name,age,adress):
        self.name=name
        self.age=age
        self.adress=adress
    def inputstu(self):
        self.name = input("请输入学生姓名：")
        self.age = input("请输入学生年龄：")
        self.adress = input("请输入学生家庭住址：")
for x in range(10):
    a=Student("","","")#注意此处，应用构造方法时，初始化时即使无信息也要给引号表示None
    a.inputstu()
    print(f"学生{x+1}信息已录入完成，姓名为{a.name},年龄为{a.age},住址为{a.adress}")