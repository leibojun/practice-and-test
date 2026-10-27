#封装，继承和多态 是面向对象编程的三大特性
#封装：将现实中的事物映射成程序中的类
#私有成员变量或者方法无法直接被类使用
class phone:
    __current_voltage = 0.67
    def __keep_single_core(self):
        print("让cpu单核运行")
    def call_by_5G(self):
        if self.__current_voltage>=0.5:
            print("电压足够，5G通信开启")
        else:
            print("电量不足")
phone1 = phone()
# phone.__keep_single_core#不能被直接使用
# print(phone1.__current_voltage)#不能被直接使用
phone1.call_by_5G()#类的内部可以自己使用私有变量和私有方法，外部则不能使用
