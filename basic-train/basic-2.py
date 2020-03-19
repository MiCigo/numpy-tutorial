'''
@Description: code
@Author: MiCi
@Date: 2020-03-18 22:40:45
@LastEditTime: 2020-03-19 23:10:50
@LastEditors: MiCi
'''

import numpy as np


class Basic2(object):

    def __init__(self):
        return

    def basic_use(self):
        a = np.arange(3)
        b = np.array([2., -1., 4.])
        print(a)
        print(np.exp(a))
        print(np.sqrt(a))
        print(np.add(a, b))
        # 函数很多看情况使用

        # 一维数组可以被索引、切片和迭代
        a = np.arange(10)**3
        print(a)
        print(a[1])
        print(a[2:5])
        print(a[::-1])

        # 多维数组每个轴有一个索引。索引由逗号分隔的元祖组成
        a = np.array([[0,  1,  2,  3],
                      [10, 11, 12, 13],
                      [20, 21, 22, 23],
                      [30, 31, 32, 33],
                      [40, 41, 42, 43]])
        print(a[1.2])
        print(a[0:5, 1])
        print(a[:, 1])
        print(a[:2, 1])
        print(a[-1])
        return


if __name__ == '__main__':
    print('Start Learn Numpy')
    print('============================\n')
    example = Basic2()
    # 通用函数ufunc
    example.basic_use()
