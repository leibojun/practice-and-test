class Record:
    def __init__(self,date,orderid,money,province):
        self.date = date
        self.orderid = orderid
        self.money = int(money)
        self.province = province
    def __str__(self):
        return f'{self.date} {self.orderid} {self.money} {self.province}'#此步让打印类对象时返回内容而非地址  魔术方法