#读取数据-》封装数据对象-》计算数据对象-》pyecharts绘图
from file_define import *
from data_define import *
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType
text_file_reader = TextFileReader(r"C:\Users\34395\Desktop\整理数据.txt")
json_file_reader = JsonFileReader(r"C:\Users\34395\Desktop\整理数据_json.txt")
tex_data:list[Record] = text_file_reader.read_data()
json_data:list[Record] = json_file_reader.read_data()
all_data:list[Record] = tex_data + json_data
#统计每日营销额
data_dict = {}
for record in all_data:
    if record.date in data_dict.keys():#当前日期已有记录，与老数据累加即可
        data_dict[record.date]+=record.money
    else:#当前日期无记录，新开一个key作为新日期
        data_dict[record.date]=record.money
print(data_dict)
print(data_dict.keys())
print(data_dict.values())
#可视化图表开发
bar = Bar()#类
bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis("销售额",list(data_dict.values()))
bar.set_global_opts(
    title_opts=TitleOpts(title = "每日销售额")
)
bar.render("每日销售额柱状图.html")