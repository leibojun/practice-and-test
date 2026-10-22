#json数据格式  组织和封装数据 本质是带有特定格式的字符串 ，负责不同编程语言之间进行数据传递和交互，类似于通用语言英语
#python->json->c++
#json的数据格式类似于字典，或者嵌套字典的列表，相当于python的字典{"key":value,"key2":value2}
import json
data=[{"name":"胡桃","age":17},{"name":"jack","age":18}]
json_str=json.dumps(data,ensure_ascii=False)#此步，数据转换为json,带后面ensure_ascii=False时，中文不会转换为asc码
print(json_str)
print(type(json_str))#列表字典被转换成了json字符串
s='[{"name":"胡桃","age":17},{"name":"jack","age":18}]'
a=json.loads(s)
print(type(a))#字符串被转换为了python中的列表
#json.dumps()转为json   json.loads()由json转为python数据
