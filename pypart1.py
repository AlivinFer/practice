# time 2019/07/14 -- 2019/07/18
# author  Fer


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
"""
# 多行注释"""  """或ctrl+/

# sequence序列
"""
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

"""

# 逻辑运算
"""
print(5 == 6) and (5 > 3)
print(not -1) or (not 0)
print(-1 == False)  # 最好不用==判断
print(0 == False)
print(5 == True)
print(5 != False)  # 一般都用！=
print(4.5/1.5)
"""

# 缩进
"""
i = 2
x = 1
if i > 0:
    x += 2
elif i < 0:
    x -= 1
elif i < 3:
    x = 5
else:
    print('you are so handsome')
print(x)
"""

# for循环
"""
# for j in [2, 7, 'smile', 3.0]:
#     print(j)
# for i in range(0, 10):
#     print(i)
# 冒泡排序(错误还未修正）
# for j in range(len(rows)):
#     for k in range(j + 1):
#         if rows[j] > rows[k]:
#             t = rows[j]
#             rows[j] = rows[k]
#             rows[k] = t
# print(rows)
"""

# 函数
"""
def square_sum(a, b):
    c = a ** 2 + b ** 2
    return c


print(square_sum(3, 4))  # 调用函数

b = [1, 2, 3]


def change_list(b):  # 表作为参数相当于指针传递（基本数据类型的参数则相当于值传递）
    b[0] = b[0] + 1
    return b


print(change_list(b))
print(b)
"""

# 面向对象的基本概念
"""
class Bird(object):
    have_feather = True  # 定义羽毛变量
    way_of_reproduction = 'egg'  # 鸟的属性

    def move(self, dx, dy):  # 定义一个方法（行为），且第一个参数必须是self
        position = [0, 0]
        position[0] = position[0] + dx
        position[1] = position[1] + dy
        return position


summer = Bird()  # 创建一个对象summer
print(summer.way_of_reproduction)  # 对属性的引用（object.attribute)
print('after move:', summer.move(5, 8))


# 继承
class Chicken(Bird):
    way_of_move = 'walk'
    possible_in_KFC = True


class Oriole(Bird):
    way_of_move = 'fly'
    possible_in_KFC = False


autumn = Chicken()
print(autumn.have_feather)
print(autumn.move(6, 10))
print(autumn.way_of_move)
"""

# 通过self来调用类的信息
"""
class Human(object):
    laugh = 'hhhhh'

    def show_laugh(self):
        print(self.laugh)

    def laugh_100th(self):
        for i in range(100):
            self.show_laugh()


Fer = Human()
Fer.laugh_100th()


# _init_方法
class man(Human):
    def __init__(self, input_name):  # 在建立对象时自动执行
        self.name = input_name

    def printName(self):
        print(self.name)


Alivin = man('Fer')
Alivin.printName()
"""

# 两个内置函数dir()和help()
"""
print(dir(list))  # 用来查询一个类或对象的所有属性
print(help(list))  # 用来查询的说明文档
"""

# list的一些常用方法
"""
n1 = [10, 12, 3, 3, 4, 15, 5, 5, 0, 9, 3]
print(n1.count(3))
print(n1.index(5))
print(n1.pop())  # 从n1中去除最后一个元素，并将该元素返回
n1.append(6)  # 在n1的最后增添一个新元素6
n1.insert(1, 9)
n1.remove(3)
n1.sort()
print(n1)
"""

# 运算符方法_add_() (内置函数）
# print([1, 2, 3] + [6, 7, 9])


# print([1, 2, 3] - [1, 2])  # 会报错，运算符"-"没用被定义
"""
class superList(list):
    def __sub__(self, b):
        a = self[:]
        b = b[:]
        while len(b) > 0:
            element_b = b.pop()
            if element_b in a:
                a.remove(element_b)
        return a


print(superList([1, 2, 3]) - superList([1, 2]))
"""

# 词典(dictionary)
"""
# 创建词典,包括键和值两部分，通过键（不可变）来引用
dic = {'tom': 11, 'sam': 18., 'fer': 23}
print(type(dic))
print(dic['tom'])
dic['sam'] = 35
print(dic)
dic['curry'] = 34  # 增加一个新的元素并赋值
print(dic)
# 循环调用(dic中元素无序）
for key in dic:
    print(dic[key])
print(len(dic))
"""

# 文本文件的输入输出
"""
# 创建文件对象
f = open('record.txt', "w")
f.write('tom, 11, 55\nsill, 12, 88\nfer, 13, 85')
f.flush()  # 清空
f.close()
x = open("record.txt", "r")
contents = x.read()
x.close()
print(contents)
"""

# 模块(一个.py文件就构成一个模块）
"""
import first

print(first.sum1(2, 3))
"""

# 包裹和解包裹
"""
# 在调用时不知道会传递多少个参数时，采用包裹(packing)传递
def func(*name):
    print(type(name))  # 所有的参数会name收集，并根据位置合并成一个元组（tuple）
    print(name)


func('sam,lil,fer')
func(1, 2, 8, 9, 10, 78)


# 传递参数是词典时使用**
def func1(**dict):
    print(type(dict))
    print(dict)


func1(a=1, b=9)
func1(m=2, n=67, k=12)


# 解包裹(unpacking)
def func2(a, b, c):
    print(a, b, c)


args = (1, 3, 5)
func2(*args)

dict1 = {'a': 1, 'b': 2, 'c': 3}
func2(**dict1)
"""

# 循环设计
"""
S = 'ascfvjhkcvhjk'
for i in range(0, len(S), 2):  # 上限、下限、步长
    print(S[i])
"""

# enumerate()函数 （枚举函数）
"""
S1 = 'zxcvbnm'
for (index, char) in enumerate(S1):
    print(index, char)
"""

# zip()函数 （若存在多个等长的序列，每次循环可从各个序列分别取出一个元素）
"""
ta = [1, 2, 3]
tb = [7, 8, 9]
tc = ['a', 'b', 'c']
for (a, b, c) in zip(ta, tb, tc):  # 从各个序列从左到右依次取出一个元素，合并成一个tuple
    print(a, b, c)
"""

# 循环对象
"""
# (__next__方法）
p = open('test1.txt', 'w')
p.write('tom, 11, 55\nsill, 12, 88\nfer, 13, 85\ngb, 24, 88')
p.flush()
p.close()
for line in open('test1.txt'):
    print(line)


# 迭代器&生成器&表推导
x1 = [1, 3, 5]
y1 = [9, 12, 13]
L = [x ** 2 for(x, y) in zip(x1, y1) if y > 10]
print(L)
"""

# map函数
"""
# lambda函数，其生成一个函数对象。map()为内置函数，有两个参数，第一个是函数对象
re = map((lambda x, y: x+y), [1, 2, 3], [6, 7, 8]) # map()返回的是循坏对象
print(re.__next__())
print(re.__next__())
print(re.__next__())
"""

# filter函数
"""
# 可通过读入的函数来筛选数据，且返回的是循坏对象
def func(a):
    if a > 100:
        return True
    else:
        return False


s1 = [10, 56, 101, 120, 112]
for i in filter(func, s1):
    print(i)
"""

# 异常处理
"""
# 类似于Java的做法
re = iter(range(5))

try:
    for i in range(10):
        print(re.__next__())
except StopIteration:
    print('here is end', i)
finally:
    print('what are you doing now')
"""


# 动态类型(类似于值传递和址传递)
# 引用和对象分离，对象是内存中存储数据的实体，引用指向对象
"""
def f(x):
    x = 100
    print(x)


a = 1
f(a)
print(a)

def f(x1):
    x1[0] = 100
    print(x1)


a1 = [1, 2, 3]
f(a1)
print(a1)
"""