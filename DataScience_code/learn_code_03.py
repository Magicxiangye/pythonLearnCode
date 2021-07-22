import enum, random

import math
from typing import Tuple


if __name__ == "__main__":

    # 验证条件概率
    # 设定python的枚举类，来设置男孩女孩的枚举类
    class Kid(enum.Enum):
        BOY = 0
        GIRL = 1


    def random_kid() -> Kid:
        return random.choice([Kid.BOY, Kid.GIRL])


    both_girls = 0
    older_girl = 0
    either_girl = 0

    # 重复随机数的种子
    random.seed(0)

    # 书上条件概率的题目---P65
    for _ in range(10000):
        younger = random_kid()
        older = random_kid()
        if older == Kid.GIRL:
            older_girl += 1
        if older == Kid.GIRL and younger == Kid.GIRL:
            both_girls += 1
        if older == Kid.GIRL or younger == Kid.GIRL:
            either_girl += 1

    print("P(both | older):", both_girls / older_girl)  # 0.514 ~ 1/2
    print("P(both | either): ", both_girls / either_girl)  # 0.342 ~ 1/3

    # 进行假设检验
    # 先是生成正态分布的mu和sigma ->来标注返回的数据的类型
    # 二项分布的mu和sigma的生成的方式
    def normal_approximation_to_binomial(n: int, p: float) -> Tuple[float, float]:
        """Returns mu and sigma corresponding to a Binomial(n, p)"""
        mu = p * n
        sigma = math.sqrt(p * (1 - p) * n)
        return mu, sigma

    # 正态累积分布函数
    # 累积分布函数是指随机变量X小于或等于x的概率
    # 公式在笔记0
    def normal_cdf(x: float, mu: float = 0, sigma: float = 1) -> float:
        return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

    # 对 normal_cdf 取逆，可以求出特定的概率的相应值
    # 使用的是二分查找，由于 normal_cdf 连续且严格递增，定位到相应的概率所需要的值
    def inverse_normal_cdf(p: float,
                           mu: float = 0,
                           sigma: float = 1,
                           tolerance: float = 0.00001) -> float:
        """Find approximate inverse using binary search"""

        # 如果非标准型，先调整单位使之服从标准型
        if mu != 0 or sigma != 1:
            return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)

        low_z = -10.0  # normal_cdf(-10)是（非常接近）0
        hi_z = 10.0  # normal_cdf(-10)是（非常接近）0

        # 这个函数反复分割区间，直到分割到一个足够接近于期望概率的精细的 Z 值。
        while hi_z - low_z > tolerance:
            mid_z = (low_z + hi_z) / 2  # 考虑中点
            mid_p = normal_cdf(mid_z)  # cdf在中点的值
            if mid_p < p:
                low_z = mid_z  # midpoint仍然太低，搜索比它大的值
            else:
                hi_z = mid_z  # midpoint仍然太高，搜索比它小的值

        return mid_z


    # 四种状态
    # 正态cdf是一个变量在一个阈值以下的概率
    normal_probability_below = normal_cdf

    # 如果它不在阈值以下，就在阈值之上
    def normal_probability_above(lo: float,
                                 mu: float = 0,
                                 sigma: float = 1) -> float:
        """The probability that a N(mu, sigma) is greater than lo."""
        return 1 - normal_cdf(lo, mu, sigma)

    #  如果它小于hi但不比lo小，那么它在区间之内
    # def normal_probability_between(lo, hi, mu=0
    def normal_probability_between(lo: float,
                                   hi: float,
                                   mu: float = 0,
                                   sigma: float = 1) -> float:
        """The probability that a N(mu, sigma) is between lo and hi."""
        return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)

    #  如果不在区间之内，那么就在区间之外
    def normal_probability_outside(lo: float,
                                   hi: float,
                                   mu: float = 0,
                                   sigma: float = 1) -> float:
        """The probability that a N(mu, sigma) is not between lo and hi."""
        return 1 - normal_probability_between(lo, hi, mu, sigma)


    def normal_upper_bound(probability: float,
                           mu: float = 0,
                           sigma: float = 1) -> float:
        """Returns the z for which P(Z <= z) = probability"""
        return inverse_normal_cdf(probability, mu, sigma)


    def normal_lower_bound(probability: float,
                           mu: float = 0,
                           sigma: float = 1) -> float:
        """Returns the z for which P(Z >= z) = probability"""
        return inverse_normal_cdf(1 - probability, mu, sigma)


    def normal_two_sided_bounds(probability: float,
                                mu: float = 0,
                                sigma: float = 1) -> Tuple[float, float]:
        """
        Returns the symmetric (about the mean) bounds
        that contain the specified probability
        """
        tail_probability = (1 - probability) / 2

        # 上界应有在它之上的tail_probability
        upper_bound = normal_lower_bound(tail_probability, mu, sigma)

        # 下界应有在它之下的tail_probability
        lower_bound = normal_upper_bound(tail_probability, mu, sigma)

        return lower_bound, upper_bound