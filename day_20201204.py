# import random
#
#
# def generate_random():
#     for i in range(10):
#         ran = random.randint(1,20)
#         print(ran)
#
#
#
# generate_random()
# import random
#
#
# def generate_random(number):
#     for i in range(number):
#         ran = random.randint(1,20)
#         print(ran)
#
#
# generate_random(5)

# def log_in(username, password):
#     for i in range(3):
#         if username == 'sunxiangyang' and password == 123456:
#             print('登录成功')
#             break
#         else:
#             print('登录失败')
#             username = input('请输入用户名')
#             password = input('请输入密码')
#     else:
#             print('账户锁定')
#
# username = input('请输入用户名')
# password = input('请输入密码')
# log_in(username,password)


def max_listValue(iterable):
    max = iterable[0]
    for i in iterable:
        if i > iterable[i]:
            max = i
    print(max)


list1 =[151,55,66,15,662,51]
max_listValue(list1)