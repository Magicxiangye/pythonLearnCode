
# 数据科学入门的第一章代码
# defaultdict的作用是在于，当字典里的key不存在但被查找时，返回的不是keyError而是一个默认值（默认就为空）
from collections import defaultdict

if __name__ == "__main__":
    interests = [
        (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
        (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
        (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
        (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
        (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
        (3, "statistics"), (3, "regression"), (3, "probability"),
        (4, "machine learning"), (4, "regression"), (4, "decision trees"),
        (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
        (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
        (6, "probability"), (6, "mathematics"), (6, "theory"),
        (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
        (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
        (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
        (9, "Java"), (9, "MapReduce"), (9, "Big Data")
    ]

    # 找出对事物共同爱好的用户的函数
    # 但是，上面的算法每次搜索都需要遍历整个兴趣列表
    # 这种算法的时间和空间成本会很大
    # 输入的是相同的兴趣
    def dataScience_who_like(target_interest):
        # 返回的还是一个数组
        return [user_id for user_id, user_interest in interests
                if user_interest == target_interest]


    # 建立一个从兴趣到用户的索引直接搜索
    user_ids_by_interest = defaultdict(list)

    # 遍历的存储兴趣到用户的索引
    for user_id, interest in interests:
        user_ids_by_interest[interest].append(user_id)