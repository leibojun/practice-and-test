if int(input("你的身高多少"))>120:
    print("过高需买票，但vip等级大于三可免费")
    if int(input("你的VIP等级是多少"))>3:
        print("尊贵的高级用户免费入园")
    else:
        print("等级不足需购票")
else:
    print("欢迎小朋友免费入园")
