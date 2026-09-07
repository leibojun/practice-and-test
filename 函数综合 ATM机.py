money=5000000
name=None#定义全局变量
name=input("请输入您的姓名")
def query(show_header):#存款阶段不显示标头，此时show_header为布尔类型变量
    if show_header:
        print("----------查询余额-----------")
    print(f"{name}您好，您的余额剩余{money}元")
def saving(num):#存款函数
    global money
    money+=num
    print("=======存款========")
    print(f"{name}您好，您存款{num}元成功")
    query(False)#使存款阶段不显示标头
def get_money(num):
    global money
    money-=num
    print("-------取款---------")
    print(f"{name}你好，您取款{num}元成功")
    query(False)
def main():
    print("-------主菜单---------")
    print(f"{name}您好，欢迎来到ATM机，请选择操作")
    print("查询余额\t输入1")
    print("存款\t\t输入2")
    print("取款\t\t输入3")
    print("退出\t\t输入4")
    return input("请输入您的选择：")
while True:
    keyboard_input=main()
    if keyboard_input == "1":
        query(True)
        continue
    elif keyboard_input == "2":
        num=int(input("您想存多少钱，请输入"))
        saving(num)
        continue
    elif keyboard_input == "3":
        num = int(input("您想取多少钱，请输入"))
        get_money(num)
        continue
    else:
        print("程序退出")
        break


