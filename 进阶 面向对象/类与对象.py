#创建对象方法  对象名 = 类名称()
#类:相当于设计图纸
#对象:由设计图纸生产的产品
#面向对象编程的思路就是设计类,生成对象,然后让对象来完成具体的工作
class Clock:
    id = None
    price = None
    def ring(self):
        import winsound
        winsound.Beep(2000,3000)
clock1 = Clock()
clock1.id="first"
clock1.price=100
print(f"闹钟id是{clock1.id},闹钟价格是{clock1.price}")
clock1.ring()