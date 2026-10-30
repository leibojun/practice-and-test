#基础对象类型注解
import json
var1: int = 10
var2 = 20 #type: int
var3 = json.loads('{"keys":"value"}') #type: dict
#类对象 类型注解
class Student():
    pass
stu: Student = Student()
#基础容器类型注解
l1:list[int] = [1,2,3]
t2:tuple[int, str,bool] = [1,"kale",True]
print(t2)
print(type(var3))
#对函数形参的类型注解
def func(data:list[int])->dict:#  ->返回值类型
    data.append(var3)
    print(data[3])
func(l1)