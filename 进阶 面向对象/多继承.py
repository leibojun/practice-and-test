#一个子类可以继承多个父类
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