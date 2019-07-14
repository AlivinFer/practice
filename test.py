# time 2019/07/14
# author  Fer
#

# 基本数据类型的操作
"""
a = 10
b = 1.2
c = True
d = 'hello'
e = 'f'
print(a)
a = 1/3
print(a)
print(a, type(a), type(b), type(c), type(d), type(e))
"""  # 多行注释"""  """或ctrl+/

# sequence序列
# sequence有两种：tuple（定值表（元组））和list（表）
# tuple的各个元素不可再变更，而list的各个元素可以再变更
s1 = (2, 1.3, 'love', 5.6, 7, False)  # s1是个tuple
s2 = [True, 6, 'smile']  # s2是个list
print(s1, type(s1))
print(s2, type(s2))
s3 = [1, [3, 4, 5]]  # 把一个序列作为另一个序列的元素
s4 = []
print(s3, s4)
# 序列的下标从0开始
print(s1[0], s1[4])
print(s3[1][0])  # 这个[1]序列相当于是固定的
s2[1] = 3.0
print(s2[1])
# s1[2] = 3  会报错，tuple的元素不能被改变
# 其他引用方式，范围引用：基本样式【下限：上限：步长】
print(s1[:5])  # 从开始到下标4，不包含下标5的元素
print(s2[1:])  # 从下标1到最后
print(s1[0:5:2])  # 从下标0到下标4，每隔2取一个元素
print(s1[2:0:-1])  # 从下标2到下标1
print(s1[-1])  # 序列的最后一个元素
print(s1[-3])  # 序列的倒数第三个元素

# 字符串是元组
str1 = 'abcdefg'
print(str1[2:4])

# 逻辑运算
print(5 == 6)and(5 > 3)
