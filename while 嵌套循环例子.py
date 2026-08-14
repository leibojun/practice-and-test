i=1
while i<=10:# 外层循环1
    print(f"今天是第{i}天，准备表白")
    j=1# 每天重置玫瑰花支数
    while j<=10:# 内层循环
        print(f"这是给小美的第{j}只玫瑰花")# 注意空格缩进
        j+=1
    print("小美我喜欢你")
    i+=1
# 输出99乘法表
k=1
while k<=9:
    l=1
    while l<=k:
        print(f"{l}*{k}={k*l} ",end='')# end表示不自动换行
        l+=1
    print('')# 换行
    k+=1