# date : 2019/07/22
# author : Fer

# python 标准库


# 1.正则表达式（编译原理）(re包)
# 可以将模糊的目标作为信息写入正则表达式
"""
import re
# search()、match()、sub()、findall()、split()函数
m = re.search('[0-9]', 'abcd56ef')  # '[0-9]'为正则表达式,搜索整个字符串，直到发现符合的子字符串
print(m.group(0))
s1 = 'a1c1ha6i3j18ki92'
n = re.match('a[0-9][a-z][0-5]', s1)  # match所匹配的开头必须符合
print(n.group(0))  # group(0)是整个正则表达的搜索结果
str1 = re.sub('1ha', 'fer', s1)  # 将搜索到的符合条件的字符串进行替换并返回
print(str1)
str2 = re.findall('[a-z][0-9]', s1)  # 搜索字符串，将所有符合的子字符串放在表（list）返回
print(str2)
str3 = re.split('[0-9]', s1)  # 分割字符串，并用表（list）返回
print(str3)
"""

# 2.时间与日期（time,datatime包）
"""
import time
import datetime
print(time.time())  # 计算机的挂钟时间(wall clock time) unit : second
print(time.perf_counter())  # 处理器时间(processor clock time) unit : second
print('start')
time.sleep(10)  # sleep for 10 seconds(设置程序睡眠时间)
print('wake up')
print(time.gmtime())  # 返回struct_time格式的UTC(世界统一时间)
print(time.localtime())
t = datetime.datetime(2019, 7, 22, 10, 26)
print(t)
"""

# 3.路径与文件(os.path包，glob包)
"""
import os.path
import glob
import shutil

path = 'E://pycharm//practice//pypart2//test_path.txt'  # 在调取路径的时候最好用/或//，使用\易造成转义
print(os.path.basename(path))  # 返回文件名
print(os.path.dirname(path))  # 返回目录路径
print(os.path.split(path))  # 分割文件名与路径
print(os.path.join('E:', 'pycharm', 'practice', 'pypart2', 'test_path.txt'))  # 合并路径
print(os.path.exists(path))  # 查询文件是否存在
print(os.path.getsize(path))  # 查询文件大小
print(os.path.getatime(path))  # 查询文件上一次读取时间
print(os.path.getmtime(path))  # 查询文件上一次修改的时间
print(glob.glob('*.py'))  # 显示当前路径下所有扩展名为py文件

# 常用函数（类似于Linux的命令）
# os.mkdir('new')
# shutil.move('test_path.txt', 'new')
# shutil.copy('test_path.txt', 'new')
"""

# 4.matplotlib库的使用
# 在导入file的时候出现了error(版本不对，未解决)
"""
import matplotlib.pyplot as plt

labels = []  # GDP
quants = []  # country name
# Read data
for line in file('country_gdp.txt'):
    info = line.split()
    labels.append(info[0])
    quants.append(float(info[1]))

plt.figure(1, figsize=(6, 6))


def explode(label, target='China'):
    if label == target:
        return 0.1
    else:
        return 0


expl = map(explode, labels)
# Colors used. Recycle if not enough.
colors = ["pink", "coral", "yellow", "orange"]
# Pie Plot
# autopct: format of "percent" string;
plt.pie(quants, explode=expl, colors=colors, labels=labels, autopct='%1.1f%%', pctdistance=0.8, shadow=True)
plt.title('Top 10 GDP Countries', bbox=dict(facecolor='0.8', pad=5))

plt.show()
"""

# 5.子进程(subprocess)
# 目前还看不懂 subprocess.Popen()、subprocess.PIPE、Popen.wait()、Popen.communicate()


# 6.信号（signal包）
# import signal
# 相关知识还不太懂，留待后面去了解


# 7.多线程与同步(后续学)
# import threading
# threading.Thread、 Lock,Condition,Semaphore,Event


# 8.当前进程信息（os包）
# get*, set*, umask(), uname()


# 9.多进程（multiprocessing包）


# 10.数学与随机数(math包, random包）
"""
import math
print(math.e)  # 自然常数e
print(math.pi)  # 圆周率Π
# math几个常用函数
x = 1.5
y = 2
print(math.ceil(x))  # 向上取整
print(math.floor(x))  # 向下取整
print(math.pow(x, y))  # 指数运算，x的y次方
print(math.log(y), math.log(100, 10))  # 默认以e为底，可以使用base来改变基底
print(math.sqrt(y))  # 平方根
print(math.sin(x))

import random
random.seed()  # 设置随机数种子
# 随机挑选和排序
s = [1, 5, 6.0, 2.5, 0, 'a', 'acd', 16]
print(random.choice(range(10)))  # 从序列的元素中随机挑选一个元素
print(random.sample(s, 5))  # 从序列中随机挑选k个元素
random.shuffle(s)  # 将序列中的元素随机排序
print(s)
# 随机生成实数
print(random.random())  # 随机生成下一个实数，在[0，1)范围内
print(random.uniform(5, 10))  # 随机生成下一个实数，在[a, b]范围内
# random.gauss(mu = , sigma =  )  # 随机生成符合高斯分布的随机数，mu和sigma为高斯分布的两个参数
# 类似的还有正太分布、对数分布等
"""

# 11.数据库(sqlite3包)
"""
import sqlite3

# test.db is a file in the working directory.
conn = sqlite3.connect("test.db")

c = conn.cursor()

# create tables
c.execute('''CREATE TABLE category
      (id int primary key, sort int, name text)''')
c.execute('''CREATE TABLE book
      (id int primary key, 
       sort int, 
       name text, 
       price real, 
       category int,
       FOREIGN KEY (category) REFERENCES category(id))''')

books = [(1, 1, 'Cook Recipe', 3.12, 1),
         (2, 3, 'Python Intro', 17.5, 2),
         (3, 2, 'OS Intro', 13.6, 2),
         ]

# execute "INSERT"
c.execute("INSERT INTO category VALUES (1, 1, 'kitchen')")

# using the placeholder
c.execute("INSERT INTO category VALUES (?, ?, ?)", (2, 2, 'computer'))

# execute multiple commands
c.executemany('INSERT INTO book VALUES (?, ?, ?, ?, ?)', books)

# save the changes
conn.commit()

# retrieve one record
c.execute('SELECT name FROM category ORDER BY sort')
print(c.fetchone())
print(c.fetchone())

# retrieve all records as a list
c.execute('SELECT * FROM book WHERE book.category=1')
print(c.fetchall())

# iterate through the records
for row in c.execute('SELECT name, price FROM book ORDER BY sort'):
    print(row)

# close the connection with the database
conn.close()
"""

# 12.特殊方法与多范式
# 特殊方法名的前后各有两个下划线
# 运算符
"""
print('abc' + 'qwe')
print(1.8.__mul__(2.0))
print(True.__or__(False))
# 内置函数
print(len([1, 2, 3]))
"""

# 13.上下文管理器
"""
# without context manager
f = open("test_path.txt", "r")
print(f.closed)            # whether the file is open
print(f.read())
f.close()
print(f.closed)

# with context manager
# 使用(with...as...)能够自动使程序块内的文件关闭
with open("test_path.txt", "r") as f:
    print(f.closed)
    print(f.read())
print(f.closed)
"""

# 14.闭包（closure）
"""
# 它是函数式编程（一种编程范式，包括面向过程和面向对象）的重要语法结构
# 函数的作用域line函数是在line_conf()里面定义的，便只能在其范围内使用
# def line_conf():
#     def line(x):
#         return 2 * x + 1
#
#     print(line(5))  # within the scope
#
#
# line_conf()
# print(line(5))  # out of the scope

# b称为line的环境变量（即line所参考的b值是函数对象定义时可供参考的b值）
# 一个函数和它的环境变量合在一起，就构成了一个闭包(closure)
def line_conf():
    b = 15

    def line(x):
        return 2 * x + b

    return line  # return a function object


b = 5
my_line = line_conf()
print(my_line(5))
print(my_line.__closure__)  # __closure__里包含了一个元组(tuple),这个元组中的每个元素是cell类型的对象
print(my_line.__closure__[0].cell_contents)  # 第一个cell包含的就是创建闭包时的环境变量b的取值


# 实例（函数line与环境变量a，c构成闭包）
# 闭包可以提高代码的可复用性，并有效的减少了所需定义的参数数目。并对并行运算有好处
def line_conf1(a, c):
    def line(x):
        return a * x + c

    return line


line1 = line_conf1(1, 1)
line2 = line_conf1(4, 5)
print(line1(5), line2(5))
"""

# 15.装饰器（decorator） ：可以对一个函数、方法或者类进行加工
"""
# get square sum
# def square_sum(a, b):
#     return a ** 2 + b ** 2
#
#
# get square diff
# def square_diff(a, b):
#     return a ** 2 - b ** 2
#
#
# print(square_sum(3, 4))
# print(square_diff(3, 4))


# 使用装饰器来修改函数的定义，为函数增加功能
def decorator(F):
    def new_F(a, b):
        print("input", a, b)
        return F(a, b)

    return new_F


# get square sum
@decorator
def square_sum(a, b):
    return a ** 2 + b ** 2


# get square diff
@decorator
def square_diff(a, b):
    return a ** 2 - b ** 2


print(square_sum(3, 4))
print(square_diff(3, 4))
"""

# 16.字符串格式化（%操作符）
"""
# 模板
a = "I'm %s. I'm %d year old" % ('Fer', 23)
print(a)
b = "My name is %(name)s. I'm %(age)d year old" % {'name': 'syq', 'age': 22}
print(b)
print("%+10x" % 10)  # 右对齐，长度为10（默认为左对齐）
print("%04d" % 5)  # 长度为4，用0来填充
print("%6.3f" % 2.3)  # 长度为6，保留小数点3位
"""

# 17.python彩蛋(python之道)
# import this
# 返回的结果为关于python的一首诗

# 18.循环器（itertools）
"""
import itertools
# 在运用循环器的时候，返回的结果用list来表示
x = itertools.count(5, 2)
print(list(itertools.islice(x, 10)))  # 从5开始的整数循环器，并设置次数
y = itertools.cycle('abc')
print(list(itertools.islice(y, 5)))  # 重复序列的元素，返回的结果为['a', 'b', 'c', 'a', 'b']
k = itertools.repeat(1.2)
print(list(itertools.islice(k, 3)))  # 重复数1.2,并设置次数
print(list(itertools.repeat(10, 5)))  # 设置循环次数
rlt = map(pow, [1, 2, 3], [1, 2, 3])  # map()根据指定的函数对序列做映射，pow()为指数函数

for num in rlt:
    print(num)

connection = itertools.chain([1, 2, 3], [4, 5, 7])  # chain()用来连接两个循环器
print(list(connection))
for m, n in itertools.product('abc', [1, 2]):  # product()返回的是多个循环器的笛卡尔积，相当于嵌套循环
    print(m, n)


def height_class(h):
    if h > 180:
        return "tall"
    elif h < 160:
        return "short"
    else:
        return "middle"


friends = [191, 158, 159, 165, 170, 177, 181, 182, 190]

friends = sorted(friends, key=height_class)
for m, n in itertools.groupby(friends, key=height_class):  # group()用来将key函数作用于原循环器的各个元素。根据key函数结果，
    # 将拥有相同函数结果的元素分到一个新的循环器。每个新的循环器以函数返回结果为标签。
    print(m)
    print(list(n))
"""

# 19.python内存管理
"""
# 对于整数和短小的字符，python会缓存这些对象，以便重复使用
a = 1
b = 1
print(id(a))  # 返回a的存储地址
# True
print(a is b)  # 用is关键字来判断所指的对象是否相同

# True
a = "good"
b = "good"
print(a is b)

# False
a = "good morning! you are so handsome"
b = "very good morning! you are so handsome"
print(a is b)

# False
a = []
b = []
print(a is b)

# 垃圾回收
import gc  # python会在特定情况下，自动启动垃圾回收

# 返回结果(700, 10, 10) # 阈值=700，后面两个10为分代回收的
print(gc.get_threshold())  # 查看阈值
# 分代回收 ：其策略是存活时间越久的对象，越不可能在后面的程序中变成垃圾。
# 因此Python将所有的对象分为0，1，2三代。所有的新建对象都是0代对象。
# 当某一代对象经历过垃圾回收，依然存活，那么它就被归入下一代对象。
# 垃圾回收启动时，一定会扫描所有的0代对象。
# 如果0代经过一定次数垃圾回收，那么就启动对0代和1代的扫描清理。
# 当1代也经历了一定次数的垃圾回收后，那么会启动对0，1，2，即对所有对象进行扫描。
"""