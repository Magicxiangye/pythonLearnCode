

# python向量的使用的技巧
from typing import List

Vector = List[float]

if __name__ == "__main__":

    # 减法也是一样的思想
    def add(v: Vector, w: Vector) -> Vector:
        """两个向量的相加"""

        # 先断言的判断一下是不是长度相等
        assert len(v) == len(w), "vectors must be the same length"

        # 调用 zip 函数，同时用列表解析
        return [v_i + w_i for v_i, w_i in zip(v, w)]


    Matrix = List[List[float]]

    A = [[1, 2, 3],  # A has 2 rows and 3 columns
         [4, 5, 6]]

    B = [[1, 2],  # B has 3 rows and 2 columns
         [3, 4],
         [5, 6]]

    from typing import Tuple

    # 自定义的查找矩阵的形状
    def shape(A: Matrix) -> Tuple[int, int]:
        """Returns (# of rows of A, # of columns of A)"""
        num_rows = len(A)
        num_cols = len(A[0]) if A else 0  # number of elements in first row
        return num_rows, num_cols

    # 自定义的获取矩阵的行和列
    assert shape([[1, 2, 3], [4, 5, 6]]) == (2, 3)  # 2 rows, 3 columns

    def get_row(A: Matrix, i: int) -> Vector:
        """Returns the i-th row of A (as a Vector)"""
        return A[i]  # A[i] is already the ith row


    def get_column(A: Matrix, j: int) -> Vector:
        """Returns the j-th column of A (as a Vector)"""
        return [A_i[j]  # jth element of row A_i
                for A_i in A]  # for each row A_i


    # typing是python3.5中开始新增的专用于类型注解(typehints)的模块，为python程序提供静态类型检查
    from typing import Callable

    # 根据shape生成矩阵
    # python类型注解，使用 -> 加类型代表返回值类型
    def make_matrix(num_rows: int,
                    num_cols: int,
                    entry_fn: Callable[[int, int], float]) -> Matrix:
        """
        Returns a num_rows x num_cols matrix
        whose (i,j)-th entry is entry_fn(i, j)
        """
        return [[entry_fn(i, j)  # given i, create a list
                 for j in range(num_cols)]  # [entry_fn(i, 0), ... ]
                for i in range(num_rows)]  # create one list for each i


    # 就可以生成一个 5×5 的单位矩阵（对角线元素是 1，其他元素是 0）
    def identity_matrix(n: int) -> Matrix:
        """Returns the n x n identity matrix"""
        # Callable，可调用类型，它通常用来注解一个方法
        # 这里用来注解的这个匿名的方法，两个参数，返回值为float
        return make_matrix(n, n, lambda i, j: 1 if i == j else 0)

    # 检验函数
    assert identity_matrix(5) == [[1, 0, 0, 0, 0],
                                  [0, 1, 0, 0, 0],
                                  [0, 0, 1, 0, 0],
                                  [0, 0, 0, 1, 0],
                                  [0, 0, 0, 0, 1]]