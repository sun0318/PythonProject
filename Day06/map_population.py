from pyecharts.charts import Map
from pyecharts import options as opts

# 数据：各省人口数量（单位：万人）
province_population = {
    '北京': 2154,
    '天津': 1560,
    '河北': 7555,
    # ... (省份及人口数据继续)

    '甘肃': 2626,
    '青海': 603,
    '宁夏': 688,
    '新疆': 2486,
}

# 处理数据，根据人口数量设置省份颜色
data = []
for province, population in province_population.items():
    if population > 2000:
        color = "#FF3333"  # 超过2000万，背景红色
    elif population > 1000:
        color = "#FFFF00"  # 超过1000万，背景黄色
    else:
        color = "#3399FF"  # 其余省份，背景蓝色
    data.append((province, population))

# 创建地图
china_map = (
    Map()
    .add("人口数量（万人）", data, maptype="china")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="中国各省人口数量分布图"),
        visualmap_opts=opts.VisualMapOpts(
            max_=max(province_population.values()),
            min_=min(province_population.values()),
            is_piecewise=True,
            pieces=[
                {"min": 2000, "color": "#FF3333"},
                {"min": 1000, "max": 2000, "color": "#FFFF00"},
                {"max": 1000, "color": "#3399FF"},
            ],
        ),
    )
)

# 渲染生成的 HTML 文件
china_map.render("china_population_map.html")
