from pyecharts.charts import *
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts

line=Line()
line.add_xaxis(["china","america","british"])#x轴
line.add_yaxis("GDP",[30,20,10])#y轴
#全局配置项
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示",pos_left="center", pos_bottom="1%"),#标题项展示
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True),
)
line.render()#生成为html网页