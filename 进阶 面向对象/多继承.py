class Phone:
    IMEI = None
    producer = "HUAWEI"
    def call_by_4G(self):
        print("4G通话")
class NFCreader:
    nfc ="第五代"
    producer = "HM"
    def readcard(self):
        print("NFC读卡")
    def writecard(self):
        print("NFC写卡")
class RemoteControler:
    rc_type = "红外遥控"
    def control(self):
        print("红外遥控开启了")
class MyPhone(Phone,NFCreader,RemoteControler):#此步继承了三个父类
    pass#表示这个新的类中不需要添加新的功能  占位用


myphone = MyPhone()
myphone.call_by_4G()
print(myphone.nfc)
myphone.readcard()
myphone.writecard()
myphone.control()
#子类可以复写父类的成员
class MyPhone2(Phone,NFCreader,RemoteControler):
    producer = "Xiaomi"#此步完成了复写成员变量操作，重新定义了producer变量
    def call_by_4G(self):#此步复写了父类中的方法
        print("4G通话（复写版）")
        print(f"{Phone.producer},此处直接引用了父类的成员变量")#可以输出，说明复写不代表覆盖，旧的数据依然可以调用输出
        Phone.call_by_4G(self)#此处调用了父类的方法 方法一
        super().call_by_4G()#调用父类方法  方法二 不用加self
p2 = MyPhone2()
p2.call_by_4G()