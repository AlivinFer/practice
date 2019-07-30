# 判断闰年以及计算2008年某月某日是这一年的第几天
# date : 2019/07/20
# author : Fer

import functools

year = int(input("请输入年份："))
if(year % 4 == 0 and year % 100 != 0)or(year % 400 == 0):
    print(year, "is leap year")
else:
    print(year, "is not leap year")
year_2008 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
mount = int(input("请输入月份：")) - 1
day = int(input("请输出日份："))
new_day = functools.reduce(lambda a, b: a+b, year_2008[:mount]) + day  # reduce函数对参数序列中的元素进行累积
print(year, '年', mount+1, '月', day, '是', year, '年中的第', new_day, '天')
