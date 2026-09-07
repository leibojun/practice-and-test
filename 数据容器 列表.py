#数据容器有五个类型
#1========================列表==============================
['a','b','c','d','e','f','g','h']#列表定义方式
name_list=['a','b','c','d','e','f','g','h']
print(name_list)
#列表支持嵌套
mylist=[[1,2,3],[4,5,6],[7,8,9]]#元素类型无限制
print(mylist[0])#打印列表中对应元素，使用了下表索引，第一个元素索引为[0]
print(mylist[1])
print(mylist[2])
#也可以反向索引
print(mylist[-1])#倒数第一个元素
print(mylist[-2])
print(mylist[-3])
#对于嵌套列表的索引
print(mylist[0][0])
print(mylist[1][0])
print(mylist[2][0])
#方法（本质上是由函数的集合，里面有很多函数可供调用）
#列表的方法(list.)
#查询元素下标的方法 "列表.index(元素)"
mylist.index([1,2,3])
a=mylist.index([4,5,6])
print(a,' 此时给出了元素[4,5,6]在mylist列表中的下标')
#列表中赋值的方法“列表[下标]=值"
mylist[0]='kale'
print(mylist,'此时mylist列表第一个元素被修改为了”kale')
#列表中元素插入操作“列表.insert(下标，元素)
newlist=[1,2,3]
newlist.insert(0,4)#新的列表中0位置放置4元素
print(newlist)
#追加元素，只能追加到尾部"列表.append（元素）"
newlist.append(5)
print(newlist)
#追加元素2，把其他数据容器追加到尾部
newlist.extend([6,7])
print(newlist)
#列表删除
#方式一del 列表[下标]
del newlist[0]
print(newlist)
#方式二 列表.pop(下标)
newlist.pop(0)
a=newlist.pop(0)
print(a,'表示删除了0号元素，注意pop方法可以读出删除元素，此处删除元素为2')
print(newlist)
#方法三 列表.remove(元素)   从头找到第一个相应元素然后删掉
newlist.remove(3)
print(newlist)
#清空列表 列表.clear()
newlist.clear()
print(newlist,' 此时为空列表')
#统计元素数量的方法 列表.count（元素）
list2=[1,2,3,3,4,4,4]
list2.count(4)
print(list2.count(4),'该列表中有3个4，所以输出3')
#统计总的元素数量 len（列表）
print(len(list2),'有7个元素，所以输出7')
#遍历列表元素
list3=[1,2,3,4,5,6]
i=0
while i<len(list3):#len(列表)获取元素数量
    a=list3[i]
    print(a,end='')
    i+=1
print('')
for i in range(0,len(list3)):
    print(list3[i],end='')
print('')
for element in list3:
    print(element,end='')



