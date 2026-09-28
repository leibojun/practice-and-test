#通过姓名找成绩？通过字典找含义？找到key的对应项，这就是字典，一一对应的“解释关系”
#{key:value,key:value,key:value.....}
dic={'xiao':169,'hutao':167,'ganyu':170}
dic2={}#定义空字典
print(dic['xiao'],"输出为’xiao'的身高")#通过key找value
#字典可嵌套
dic_3={'xiao':{'height':169,'weight':65},'hutao':{'height':167,'weight':60},'ganyu':{'height':170,'weight':61}}
print(dic_3['hutao']['weight'])#嵌套字典的数据查询