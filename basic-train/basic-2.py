'''
@Description: code
@Author: MiCi
@Date: 2020-03-18 22:40:45
@LastEditTime: 2020-03-22 22:38:15
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

    def basic_use2(self):
        a = np.floor(10*np.random.random((3, 4)))
        print(a)
        print(a.shape)
        # 数组形状修改
        print(a.ravel())
        a.shape = (6, 2)
        a.transpose()
        print(a)
        a.resize((2, 6))
        print(a)

        # 组合数组
        a = np.floor(10*np.random.random((2, 2)))
        b = np.floor(10*np.random.random((2, 2)))
        print(np.vstack((a, b)))
        print(np.hstack((a, b)))
        # column_stack以列将一维数组合成二维数组
        print(np.column_stack((a, b)))
        # newaxis划分为多行
        a = np.array([4., 2.])
        print(a[:, np.newaxis])

        # 分割数组，vsplit沿着纵向轴分割
        a = np.floor(10*np.random.random((2, 12)))
        print(a)
        print(np.hsplit(a, 3))
        print(np.hsplit(a, (3, 4)))

        # 完全不拷贝，简单赋值不拷贝数组对象及数据
        a = np.arange(12)
        b = a
        print(b is a)
        b.shape = 3, 4
        print(a.shape)

        # 浅复制，不同数组对象分享同一个数据，用视图创造一个新的数组对象指向同数据
        c = a.view()
        print(c is a)
        print(c.base is a)
        c.shape = 3, 4
        print(a.shape)
        c[0, 1] = 6666
        print(a)

        # 深复制，完全复制数组和数据
        d = a.copy()
        print(d is a)
        print(d.base is a)
        d[0, 1] = 6666
        print(a)

        return


if __name__ == '__main__':
    print('Start Learn Numpy')
    print('============================\n')
    example = Basic2()
    # 通用函数ufunc
    # example.basic_use()
    # 形状操作
    example.basic_use2()
