'''
@Description: code
@Author: MiCi
@Date: 2020-03-16 21:31:24
@LastEditTime: 2020-03-18 23:36:29
@LastEditors: MiCi
'''

import numpy as np


class Basic1(object):

    def __init__(self):
        return

    def basic_use(self):
        # Numpy主要对象是同种元素的多维数组，维度叫做轴（axes），轴的个数叫做秩（rank）
        # 数组类：ndarray，属性： ndim、shape、size、dtype、itemsize、data
        testArray = np.arange(20).reshape(4, 5)
        print(testArray)
        print(type(testArray))

        # 秩
        print(testArray.ndim)
        # 维度，n排m列（n,2）
        print(testArray.shape)
        # 元素的总个数
        print(testArray.size)
        # 元素总类型对象
        print(testArray.dtype)
        # 元素字节大小
        print(testArray.itemsize)

        # 创建数组，就是用list以及元祖
        testArray_1 = np.array([1, 2, 3])
        print(testArray_1.dtype)
        testArray_2 = np.array([1.2, 2, 3.1])
        print(testArray_2.dtype)
        testArray_3 = np.array([(1.2, 2, 3), (4, 5, 6)])
        print(testArray_3.dtype)

        # 占位符创建数组函数，ones、empty、zeros，默认类型均为float64
        testArray_4 = np.zeros((3, 4))
        print(testArray_4)
        testArray_5 = np.ones((2, 3, 4), dtype='int32')
        print(testArray_5)
        testArray_6 = np.empty((2, 3))
        print(testArray_6)

        # 利用arange返回数组
        testArray_7 = np.arange(10, 20, 2)
        print(testArray_7)
        testArray_8 = np.arange(0, 2, 0.3)
        print(testArray_8)
        # 还有其他诸多函数：rand等

        # np数组打印布局：
        # 最后的轴从左到右打印
        # 次后的轴从顶向下打印
        # 剩下的轴从顶向下打印，每个切片通过一个空行与下一个隔开
        # 一维数组被打印成行，二维数组成矩阵，三维数组成矩阵列表。
        print(np.arange(24).reshape(2, 3, 4))
        print(np.arange(10000).reshape(100, 100))

        return

    def basic_use2(self):
        # 按元素进行运算
        a = np.array([20, 30, 40, 50])
        b = np.arange(4)
        print(a)
        print(b)
        print(a-b)
        print(b**2)
        print(10*np.sin(a))
        print(a < 35)

        # *号按元素计算，矩阵计算用dot函数
        a = np.array([[1, 1],
                      [0, 1]])
        b = np.array([[2, 0],
                      [3, 4]])
        print(a*b)
        print(np.dot(a, b))

        # 运算不同类型数组，结果数组使用更准确类型
        a = np.ones(3, dtype='int32')
        b = np.linspace(0, np.pi, 3)
        print(b.dtype.name)
        print((a+b).dtype.name)

        # 数组求和、最大值、最小值
        a = np.random.random((2, 3))
        print(a)
        print(a.sum())
        print(a.max())
        print(a.min())

        # 指定axis运算位置
        a = np.arange(12).reshape(3, 4)
        print(a)
        print(a.sum(axis=0))
        print(a.min(axis=1))
        print(a.max(axis=1))
        # 累加
        print(a.cumsum(axis=1))
        return


if __name__ == '__main__':
    print('Start Learn Numpy')
    print('============================\n')
    example = Basic1()
    # 最基本信息
    # example.basic_use()
    # 基本运算
    example.basic_use2()
