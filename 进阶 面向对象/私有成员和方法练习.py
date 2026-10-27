class Phone:
    __is_5G_enable = True
    def __check_5G(self):
        if self.__is_5G_enable:
            print("5G is OK")
        else:
            print("5G is not OK,using 4G")
    def call_by_5G(self):
        self.__check_5G()
        print("正在通话中")
phone1 = Phone()#构建类对象
phone1.call_by_5G()
#私有变量或者方法前面加两条下划线__即可
