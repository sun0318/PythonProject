# 导包，导入Line功能构建折线图对象
from pyecharts.charts import *

# 得到折线图对象
from pyecharts.options import TitleOpts
from pyecharts.options import LegendOpts
from pyecharts.options import ToolboxOpts
from pyecharts.options import VisualMapOpts
from pyecharts.options import TooltipOpts

line = Line()
# 添加X轴数据
line.add_xaxis(["中国", "新加坡", "新西兰"])
# 添加Y轴数据
line.add_yaxis("GDP", ["30", "20", "10"])
# 设置全局配置项 set_global_opts 来设置
line.set_global_opts(
    title_opts=TitleOpts(title="2022年全球GDP", pos_bottom=0, pos_left="center"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True),
    tooltip_opts=TooltipOpts(is_show=True)

)

# 生成图表
line.render(path="paragraph1.html")