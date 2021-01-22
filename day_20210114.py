#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：code 
@File ：day_20210114.py
@Author ：sunxiangyang
@Date ：2021-01-14 14:51 
'''


# count = 0
# def test():
#     global count
#     count +=1
#     print('123')
#     print('456')
#     print('789')
#     if count < 5:
#         test()
#
# test()

# def get_sum(n):
#     if n == 0:
#         return 0
#     if n < 0:
#         return ('输入错误')
#     return n + get_sum(n - 1)
#
#
# print(get_sum(8))
#

# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)
#
#
# print(factorial(6))

# def fibonacci(n):
#     if n == 1 or n==2:
#         return 1
#     return fibonacci(n-2)+fibonacci(n-1)
#
#
# print(fibonacci(8))
#
# get_sum = lambda a,b: a+b
#
# print(get_sum(4,5))
import functools

# students = [
#     {'name': 'zhangsan', 'age': 18, 'score': 92},
#     {'name': 'lisi', 'age': 20, 'score': 90},
#     {'name': 'wangwu', 'age': 19, 'score': 95},
#     {'name': 'jerry', 'age': 21, 'score': 98},
#     {'name': 'chris', 'age': 17, 'score': 100},
# ]
# # print(type(students))
#
# students.sort(key=lambda stu: stu['score'])
# print(students)
#
ages = [12,36,54,68,8,9,14,8,4,6]
# def age():
#     for i in ages:
#         if i > 8:
#             return i
#
#
# print(age())
num = filter(lambda ele : ele >18 ,ages)
for i in num:
    print(i)


