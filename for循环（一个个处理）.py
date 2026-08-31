# for 临时变量 in 待处理数据集:  为其基础语法   临时变量规范上只能在循环内部使用
name="battlefield"# 定义了一个字符串
count=0
for x in name:# 遍历字符串
    print(f"{x} ",end='')# 把每个字符单独输 end=''表示不自动换行
    if(x=="e"):
        count+=1
print(f'\ncount={count}')# 统计了字符e的数量
# range语句
#语法一 range(num)===>[0,1,2,3,4...,num-1]
#语法二 eg.range(5,10)===>[5,6,7,8,9]
#语法三 range(num1,num,step) eg.range(5,10,2)===>[5,7,9]步长为2，依旧取到num-1
for x in range(5,10):
    print(x,end='')
print("")
for x in range(5,10,2):
    print(x,end='')
print('')
# for x in range(num)语句本身可以作为循环语句使用
oushu=0
for x in range(1,100):
    if(x%2==0):
        oushu+=1
print(f"偶数个数为{oushu}")

