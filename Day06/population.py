from pyecharts.charts import Bar
from pyecharts import options as opts

# 数据：国家和人口数量（单位：百万）
countries = ['China', 'India', 'United States', 'Indonesia', 'Pakistan', 'Brazil', 'Nigeria', 'Bangladesh', 'Russia', 'Mexico']
populations = [1444216, 1393409, 332915, 276361, 225200, 213993, 211400, 166303, 145912, 130262]

# 创建柱状图
bar = (
    Bar()
    .add_xaxis(countries)
    .add_yaxis("Population (Millions)", populations, label_opts=opts.LabelOpts(position="inside"))
    .set_global_opts(title_opts=opts.TitleOpts(title='Top 10 Most Populous Countries in the World'))
)

# 渲染生成的 HTML 文件
bar.render("bar_chart.html")
