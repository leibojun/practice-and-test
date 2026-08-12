import random
num=random.randint(1,100)
count=0
flag=True
while flag:
    count+=1
    guess=int(input("请输入猜测数字："))
    if num==guess:
        print("correct！")
    else:
        if num<guess:
            print("too big")
        else:
            print("too small")
print(f"你猜了{count}次")