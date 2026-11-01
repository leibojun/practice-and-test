#定义一个抽象类做顶层设计，确定有哪些功能需要实现
from data_define import Record
import json
class FileReader:
    def read_data(self)->list[Record]:
        #把文件数据转换成Record类对象，把他们封装到list内返回,list里的元素是Record类对象
        pass
class TextFileReader(FileReader):
    def __init__(self, path):#构造方法定义成员变量
        self.path = path
    def read_data(self)->list[Record]:#复写（实现抽象方法）
        f = open(self.path,'r',encoding='utf-8')#方法内部使用成员变量要加self.
        record_list = []
        for line in f.readlines():
            line = line.strip()#消除回车换行符
            data_list =line.split(",")
            record = Record(data_list[0],data_list[1],int(data_list[2]),data_list[3])#构建了一个类对象
            record_list.append(record)
        f.close()
        return record_list
class JsonFileReader(FileReader):
    def __init__(self, path):
        self.path = path
    def read_data(self)->list[Record]:
        f = open(self.path, 'r', encoding='utf-8')  # 方法内部使用成员变量要加self.
        record_list = []
        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict['date'],data_dict['orderid'],int(data_dict['money']),data_dict['province'])
            record_list.append(record)
        f.close()
        return record_list
if __name__ == '__main__':
    text1 = TextFileReader(r"C:\Users\34395\Desktop\整理数据.txt")
    text2 = JsonFileReader(r"C:\Users\34395\Desktop\整理数据_json.txt")
    list1 = text1.read_data()
    list2 = text2.read_data()
    for x in list1:
        print(x)
    for x in list2:
        print(x)


