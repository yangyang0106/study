# dict = {'赵四':1,'王五':2,'孙刘':3,'阿水':4,'武器':5}
# del dict['赵四']
# print(dict)
#
# d1 = dict.pop('王五')
# print(dict)
# d2 = dict.popitem()
# print(dict)
# dict.clear()
# print(dict)
# s1 =set()
# list1 = [5,1,6,5144,11,55,66,44,22,33,4,4,55,16,66]
# print(set(list1))
#
# s1.add('ab')
# s1.add('cd')
# s1.add('ef')
#
# t1 = ('gh','qw','er')
# s1.update(t1)
#
#
# print(s1)
#
# s1.remove('gh')
# print(s1)
# s1.pop()
# print(s1)



# import random
# in_num = int(input("输入"))
# print()
# num = set()
# print(num)
# for i in range(20):
#    num.add(random.randint(0,20))
#    print(num)
#    if in_num in num:
#        print()
#        num.remove(in_num)
# print(num)

#
# import turtle
#
#
# # 定义圣诞树的绿叶函数
# def tree(d, s):
#     if d <= 0:
#         return
#     turtle.forward(s)
#     tree(d - 1, s * .8)
#     turtle.right(120)
#     tree(d - 3, s * .5)
#     turtle.right(120)
#     tree(d - 3, s * .5)
#     turtle.right(120)
#     turtle.backward(s)
#
#
# n = 100
# """ 设置绘图速度
# 'fastest' :  0
# 'fast'    :  10
# 'normal'  :  6
# 'slow'    :  3
# 'slowest' :  1
# """
# turtle.speed('fastest') # 设置速度
#
# turtle.left(90)
# turtle.forward(3 * n)
# turtle.color("orange", "yellow")
# turtle.left(126)
#
#
# # turtle.begin_fill()
# for i in range(5):
#     turtle.forward(n / 5)
#     turtle.right(144)
#     turtle.forward(n / 5)
#     turtle.left(72)
#     turtle.end_fill()
# turtle.right(126)
# turtle.color("dark green")
# turtle.backward(n * 4.8)
#
# # 执行函数
# tree(15, n)
# turtle.backward(n / 5)


# import turtle
#
# screen = turtle.Screen()
# screen.setup(375, 700)
#
# circle = turtle.Turtle()
# circle.shape('circle')
# circle.color('red')
# circle.speed('fastest')
# circle.up()
#
# square = turtle.Turtle()
# square.shape('square')
# square.color('green')
# square.speed('fastest')
# square.up()
#
# circle.goto(0, 280)
# circle.stamp()
#
# k = 0
# for i in range(1, 13):
#     y = 30 * i
#     for j in range(i - k):
#         x = 30 * j
#         square.goto(x, -y + 280)
#         square.stamp()
#         square.goto(-x, -y + 280)
#         square.stamp()
#
#     if i % 4 == 0:
#         x = 30 * (j + 1)
#         circle.color('red')
#         circle.goto(-x, -y + 280)
#         circle.stamp()
#         circle.goto(x, -y + 280)
#         circle.stamp()
#         k += 3
#
#     if i % 4 == 3:
#         x = 30 * (j + 1)
#         circle.color('yellow')
#         circle.goto(-x, -y + 280)
#         circle.stamp()
#         circle.goto(x, -y + 280)
#         circle.stamp()
#
# square.color('brown')
# for i in range(13, 17):
#     y = 30 * i
#     for j in range(2):
#         x = 30 * j
#         square.goto(x, -y + 280)
#         square.stamp()
#         square.goto(-x, -y + 280)
#         square.stamp()