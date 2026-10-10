#通过姓名找成绩？通过字典找含义？找到key的对应项，这就是字典，一一对应的“解释关系”
#{key:value,key:value,key:value.....}
dic_demo=dict()#定义空字典方式一
dic={'xiao':169,'hutao':167,'ganyu':170}
dic2={}#定义空字典方式二
print(dic['xiao'],"输出为’xiao'的身高")#通过key找value
#字典可嵌套
dic_3={'xiao':{'height':169,'weight':65},'hutao':{'height':167,'weight':60},'ganyu':{'height':170,'weight':61}}
print(dic_3['hutao']['weight'])#嵌套字典的数据查询
#新增元素dic[key]=value,若已有元素，则实现修改值的操作
dic['weisina']=166
print(f'威斯纳的身高是{dic['weisina']}')
#删除元素  既能删除又能获得被删除的值dic.pop()
height=dic.pop('hutao')
print(f'被删除的是胡桃的身高{height}')
#获得全部key   字典.keys()
keys=dic_3.keys()
print(keys)
#遍历字典
for key in keys:#注意字典不支持下标索引，所以不能用while循环
    print(f'字典的key是{key}')
    print(f'字典的value是{dic_3[key]}')
for key in dic_3:#遍历方式二，直接 in 字典
    print(f'字典的key是{key}')
    print(f'字典的value是{dic_3[key]}')
num=len(dic_3)
print(f'字典里的元素有{num}个')