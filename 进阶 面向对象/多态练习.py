class AC:
    def coolwind(self):
        pass#制冷功能
    def hotwind(self):
        pass#制热功能
    def swing(self):
        pass#摆风功能
class meidi(AC):
    def coolwind(self):
        print("coolwind美的")
    def hotwind(self):
        print("hotwind美的")
    def swing(self):
        print("swing美的")
class geli(AC):
    def coolwind(self):
        print("coolwind格力")
    def hotwind(self):
        print("hotwind格力")
    def swing(self):
        print("swing格力")
def func(ac:AC):#传入父类对象，表示“有什么功能”
    ac.coolwind()
    ac.hotwind()
    ac.swing()
mac = meidi()#创建类对象注意加括号
gac = geli()
func(mac)
func(gac)