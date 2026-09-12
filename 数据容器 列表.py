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
    print(element)
#找偶数练习
nums=[1,2,3,4,5,6,7,8,9,10]
newnums_list1=[]
i=0
while i<len(nums):
    if nums[i]%2==0:
        newnums_list1.append(nums[i])#数组增加操作
    i+=1
print(newnums_list1,'此时为while循环做到')
newnums_list2=[]
for ele in nums:#for循环的使用技巧，可以直接遍历元素本身而非访问下标
    if ele%2==0:
        newnums_list2.append(ele)
print(newnums_list2,'此时为for循环做到')
#=================元组================================================
#遇到不可以被篡改数据的要求，则可以定义为元组，元组内部数据不可篡改
t1=(1,2,3,4,5)
t2=tuple(t1)
t3=()#空元组
t4=('hello',)#注意后面有个逗号,此时才是元组
#上面4个都是用变量接收元组的例子z
print(t1,t2,t3)
print(type(t1),type(t2),type(t3))
t5=(t1,t2,t3)#元组可嵌套
print(t5)
print(t5[1][2],'这一步是读取对应位置上的值')#读出元组中的值
#元组中相关操作
print(t1.index(4))#按照值读取位置
print(t1.count(3))#计算元素3出现次数
print(len(t1))#计算元组长度
#特例元组里面有列表的话可以修改
t9=(1,2,[3,4,5])
t9[2][2]='hello'
print(t9)
#==================字符串=================
#字符串支持下标索引
str='123456'
print(str[3],'此时会打印“4”')
#字符串是无法修改的字符容器
#index可给出一个单词的起始下标
#字符串替换操作，注意此时得出了一个新的字符串，老字符串无法修改
a='123 456'
b=a.replace('456','789')#用789去代替456
print(b)
a='abc def'
b=a.split(' ')#字符串切割操作
print(b)#按照特定分隔符号进行切割，得出了一个列表
#规整操作
str=('   12 aabbcc 21')
newstr=str.strip()#前后空格和换行符去除
print(newstr)
newstr2=newstr.strip('12')#指定1和2两个小字符去除，与顺序无关
print(newstr2)
print(newstr.count('b'))#统计字符b在字符串中出现次数
print(len(newstr))#长度统计，跟前面语法一致




