# s1 = input('请输入一个单词:')
# i = 0
# for i in range(len(s1))[:-1]:
#     print(i)
#     if s1[i] <'A' or s1[i] >'Z':
#         print('小易不喜欢这些单词')
#         break
#     elif s1[i] == s1[i+1]:
#         print('小易不喜欢这些单词')
#         break
#     else:
#         print('小易喜欢这些单词')
#



while True:
    username = input('请输入用户名')
    password = input('请输入用户密码')
    mail = input('请输入邮箱')
    username= username[0:20]
    password=password[0:20]
    mail=mail[0:20]
    msg = ('用户名为:{}\n密码为{}\n邮箱为:{}\n'.format(username,password,mail))

    if username == 'q' or password== 'q' or mail== 'q':
        break
print(msg)