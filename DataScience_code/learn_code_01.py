from matplotlib import pyplot as plt
from collections import Counter


if __name__ == "__main__":
    years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
    gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

    # 折线图
    plt.plot(years, gdp, color="green", marker='o', linestyle='solid')
    plt.title("GDP")

    # y轴的标记
    plt.ylabel("bililion")
    plt.show()

    # 条形图
    movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
    num_oscars = [5, 11, 3, 8, 10]

    # 条形的默认宽度是0.8，因此我们对左侧坐标加上0.1
    # 这样每个条形就被放置在中心了
    xs = [i + 0.1 for i, _ in enumerate(movies)]
    # 使用左侧x坐标[xs]和高度[num_oscars]画条形图
    plt.bar(xs, num_oscars)

    plt.ylabel("movies")
    plt.title("like movies")

    # 使用电影的名字标记x轴，位置在x轴上条形的中心
    plt.xticks([i + 0.1 for i, _ in enumerate(movies)], movies)

    plt.show()

    # 分布图
    grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]

    # 统计每个分数段的总数
    histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)

    # 定义图表中的长宽高
    # 每个条形向右侧移动1个单位
    # 给每个条形设置正确的高度
    # 每个条形的宽度设置为8
    plt.bar([x + 1 for x in histogram.keys()], histogram.values(), 8)

    # xy轴的取值的范围
    plt.axis([-5, 105, 0, 5])

    # x轴标记为0，10，...，100
    plt.xticks([10 * i for i in range(11)])
    plt.xlabel("grades")
    plt.ylabel("student numbers")
    plt.title("work")

    plt.show()

    mentions = [500, 505]
    years = [2013, 2014]

    # 还是直方图
    plt.bar([2012.6, 2013.6], mentions, 0.8)
    plt.xticks(years)
    plt.ylabel("num")

    # 如果不这么做，matplotlib会把x轴的刻度标记为0和1
    # 然后会在角上加上+2.013e3（糟糕的matplotlib操作！）
    # plt.ticklabel_format(useOffset=False)
    plt.axis([2012.5, 2014.5, 0, 550])
    plt.title("条形图")
    plt.show()

    # 多线图
    # 用来清晰地显示某种事物的趋势
    variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
    bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
    total_error = [x + y for x, y in zip(variance, bias_squared)]
    xs = [i for i, _ in enumerate(variance)]

    # 可以多次调用plt.plot
    # 以便在同一个图上显示多个序列
    # 绿色实线
    plt.plot(xs, variance, 'g-', label='variance')
    # 红色点虚线
    plt.plot(xs, bias_squared, 'r-.', label='bias')
    # 蓝色点线
    plt.plot(xs, total_error, 'b:', label='total')

    # 可以自由地布置图例
    # loc=9指的是“顶部中央”
    plt.legend(loc=9)
    plt.xlabel("模型复杂度")
    plt.title("偏差-方差权衡图")
    plt.show()

    # 散点图
    # 散点图是显示成对数据集的可视化关系的好选择

    friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
    minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

    # 散点图的生成
    plt.scatter(friends, minutes)

    # 给每一个的点加上标记
    for label, friend_counts, minute_count in zip(labels, friends , minutes):
        # 把标记放在对应的点上
        # 但要有轻微偏离
        plt.annotate(label, xy=(friend_counts, minute_count), xytext=(-5, 5), textcoords='offset points')

    plt.show()

    test_1_grades = [99, 90, 85, 97, 80]
    test_2_grades = [100, 85, 60, 90, 70]
    plt.scatter(test_1_grades, test_2_grades)
    plt.title("Axes Are Comparable")
    # 引入对 plt.axis（"equal"）的调用,会更精确地显示大多数变化发生在哪一个数据上
    plt.axis("equal")
    plt.xlabel("test 1 grade")
    plt.ylabel("test 2 grade")

    plt.show()





