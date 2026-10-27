#继承相当于复制粘贴然后稍作修改
class Phone:
    IMEI = None
    producer = "HUAWEI"
    def call_by_4G(self):
        print("4G通话")
#单继承
class Phone2(Phone):
    face_id = True
    def call_by_5G(self):
        print("2022最新5G通话")
phone2022= Phone2()
phone2022.call_by_5G()
phone2022.call_by_4G()
print(phone2022.producer, "面部识别:",phone2022.face_id)
