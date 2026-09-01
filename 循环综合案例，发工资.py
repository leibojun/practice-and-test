money=10000
for i in range(1,21):#给20个员工发工资
    import random
    score=random.randint(1,10)#员工的绩效分（1到10随机）
    if score<5:
        print(f"员工{i}绩效分{score}，不满足，下一位")
        continue#跳过发放，从循环第一步开始继续
    if money>=1000:#判断余额足不足
        money-=1000
        print(f"员工{i}，满足条件发放工资1000元，公司账户余额{money}")
    else:
        print(f"余额不足，当前余额{money}元，不足以发工资")
        break#工资发完结束循环