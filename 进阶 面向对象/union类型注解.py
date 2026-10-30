from typing import Union
my_list: list[Union[int,str]] = [1,2,3,"string"]
print(my_list)
print(type(my_list))
#函数中也能使用Union类型注解
def func(data:Union[int,str])->Union[int,str]:
    pass
func()