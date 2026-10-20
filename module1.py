def func1(a,b,c):
    print(a+b*c)
def func2(a,b,c):
    print(a+b-c)
if __name__ == '__main__':#在模块内部可用于测试摸块功能，调用模块时不会输出其下面的内容
    func1(1,2,4)
__all__ = ['func1']#这个只会限制用*导入全部功能的情况，此时不包含func2，但是func2可以手动导入