# date : 2019/07/18
# author : Fer
# -*- coding: utf-8 -*

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path = 'ex1data1.txt'
data = pd.read_csv(path, header=None, names=['Population', 'Profit'])  # 读取文件
# header指定哪一行作为表头，默认为None，names用来设置列的名称
print(data.head(20))  # 默认读取前五行

data.describe()
data.plot(kind='scatter', x='Population', y='Profit', figsize=(10, 8))  # plot()方法用来绘制带有标签的所有列
# x、y:数据框列的标签；kind：指定图的类型(scatter：离散型)；figszie:指定窗口大小)
plt.show()


def computeCost(x, y, theta):
    inner = np.power(((x * theta.T) - y), 2)  # np.power()数组元素求n次方，返回的是array类型(theta.T表示转置)
    return np.sum(inner) / (2 * len(x))


data.insert(0, 'Ones', 1)  # 在第一列插入数据

cols = data.shape[1]  # 取列数cols = 3
x = data.iloc[:, 0:cols - 1]  # 取第一列和cols-1列(前开后闭)
y = data.iloc[:, cols - 1:cols]

x.head()
y.head()

# x = np.matrix(x.values) 使用matrix会warning，用mat
x = np.mat(x.values)
y = np.mat(y.values)
theta = np.mat(np.array([0, 0]))

# theta
# X.shape, theta.shape, y.shape
computeCost(x, y, theta)
print(x)
print(y)
print(theta)

