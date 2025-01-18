from pyecharts import options as opts
from pyecharts.charts import Pie

# 生成五个电脑品牌的销售量数据（示例数据）
brands = ['Brand A', 'Brand B', 'Brand C', 'Brand D', 'Brand E']
sales = [350, 450, 300, 600, 400]  # 销售量

# 创建饼图实例
pie_chart = (
    Pie()
    .add(
        "",
        [list(z) for z in zip(brands, sales)],
        radius=["40%", "75%"],  # 设置内外半径，以控制饼图大小
        label_opts=opts.LabelOpts(
            position="outside",
            formatter="{b}: {d}%"  # 设置标签格式，显示品牌名称和销售量占比
        ),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Sales Distribution of Computer Brands in a Month"))
)

# 生成并保存图表
pie_chart.render("sales_distribution.html")
