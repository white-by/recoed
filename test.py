from pyecharts.charts import Bar
from pyecharts import options as opts

fruits = ['apple', 'banana']
counts = [2, 3]

# 创建 Bar 实例
bar = Bar()

# 添加 x 轴和 y 轴数据
bar.add_xaxis(fruits)
bar.add_yaxis('数量', counts)

# 设置全局配置项
bar.set_global_opts(
    # 标题
    title_opts=opts.TitleOpts(title='水果数量柱形图'),
    # X 轴标签旋转角度
    xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=0))
)

# 设置系列配置项
bar.set_series_opts(
    # 标签显示在柱形图内部
    label_opts=opts.LabelOpts(position='inside')
)

# 绘图
bar.render('fruit_bar_chart.html')
