#len() max() min()
#类型转换
tuple1=(3,2,1,4,5)
list1=list(tuple1)
print(list1)
tuple2=tuple(list1)
print(tuple2)
#通用排序功能 sorted(list)
print(sorted(list1))#排序结果为列表对象,最后得到一个列表
#反向排序
print(sorted(list1,reverse=True))