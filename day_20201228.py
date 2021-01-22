# list1 = [1,3,5,9,7,0]
# list2 = list1
# list1.remove(5)
# print(list2)

# def add(name,*args):
#     sum = 0
#     if len(args) > 0:
#         for i in args:
#             sum += i
#         print('%s累加和是：sum:%s' % (name,sum))
#     else:
#         print("没有元素可计算，sum:" , sum)
#
# add('狒狒',5,8,6,9)

# def add(a,b=10):
#     result = a+ b
#     print(result)
#
# add(5)


# students = {'001':('蔡徐坤',21),'002':('王源',19),'003':('王俊凯',20),'004':('易烊千玺',19)}
# def print_boy(persons):
#     if isinstance(persons,dict):
#         values = persons.values()
#         print(values)
#         for name,age in values:
#             print('{}的年龄是:{}'.format(name,age))
#
# # print_boy(students)
#
# def func(**kwars):
#     print(kwars)
#
#
# func(a= 1, b=2 ,c =3)
#
#
#
# def aa(a,b,*c,**d):
#     print(a,b,c,d)
#
# aa(1,2


# def func(a,*args):
#     print(a,args)
#
# func(2,3,4,5)
# print('******************************')
# func(2,[1,2,3,4])
# print('******************************')
# func(2,3,[1,2,3,4,5])
# print('******************************')
# func(5,6,(4,5,6),9)

# def func(a,b=10,c=3,**kwargs):
#     print(a,b,c,kwargs)
#
# func(1) # 1 10 3 {}
# print('******************************')
# func(2,b=10) # 2 10 3 {}
# print('******************************')
# #func(3,5,7,a=1,b=2) 报错
#

def func(a,*args,**kwargs):
    print(a,args,kwargs)


t=(1,2,3,4)
func(1,t)  ###1 ((1, 2, 3, 4),) {} 

l = [2,5,8]
func(1,1,a=9,b =6) #错误








