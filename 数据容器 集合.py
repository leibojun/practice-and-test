#集合不支持元素重复，而且无序，能够做到去重任务
set={1,1,2,3,4}#定义了一个集合
print(set)#此时输出1234，自动去重
print(type(set))
#集合.add可添加新元素
set.add(5)
print(f"添加元素后的新集合为{set}")
#集合.remove可删除元素
set.remove(5)
print(f"移除5后的集合为{set}")
#集合.pop随机取出元素
a=set.pop()
print(a)
#clear清空集合
set.clear()
print(f"集合被清空了,结果是{set},意思是空集合")
#取差集
set1={1,2,3,4,5}
set2={3,4,5,6,7}
set3=set1.difference(set2)#set1而set2没有的元素
print(set3)
set1.difference_update(set2)
print(set1)#集合一被修改了,差集运算与difference一致,区别在于修改了set1本身
#union语句合并集合
set4=set1.union(set2)#合并两个集合
print(set4)
#不能用while遍历,但是可以用for遍历
for item in set4:
    print(item)

    #下面是去重小练习
    set.clear()
list=[1,2,3,4,5,5,5,4,4,6,7]
for item in list:
    set.add(item)
print(set)