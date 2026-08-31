#坚持表白一百天，每天送10朵花
for i in range(1,101):#不包含101
    print(f"今天是表白第{i}天，加油坚持")
    for j in range(1,11):
        print(f"给小美的第{j}朵玫瑰花")
    print('小美我喜欢你')
print('表白成功')# 注意缩进层次关系
#九九乘法表打印（用for循环）
for i in range(1,10):#外层循环控制行
    for j in range(1,i+1):#这里只能读到1，2，3.。。一直到i，读不到i＋1这个数字
        print(f'{j}*{i}={i*j}\t',end='')#\t为列对齐命令
    print('')#换行
#continue 关键字
for i in range(1,6):
    print('语句一')
    continue
    print('语句二')
#break关键字 直接结束循环
for i in range(1,6):
    print('语句三')
    break#此步循环停止，整体全部结束
    print('语句四')
#break和continue只在所在循环内生效
