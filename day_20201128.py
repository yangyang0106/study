'''print('*' * 10, '欢迎来到消消乐', '*' * 10)
level = input('请输入你的级别（lv1,lv2）:')
if level == 'lv1':
    print('免费玩，随便玩')
else:
    print('已经进入付费级别，请充值')
    money = input('请充值（充值金额必须为100的倍数）:')
    if int(money) % 100 == 0 and int(money) > 0:
        print('充值金额为', money)
    else:
        print('充值失败请重新充值')'''



''' import random
    
ran_num = random.randint(1, 50)
while (True):
value = input('请输入你要猜测的值:')
    if int(value) == ran_num:
        print('恭喜你猜对了值为', ran_num)
        break
        elif int(value) < ran_num:
        print('你猜小了重新猜测')
        else:
        print('你输入的值大了请重新输入')'''



'''for i in range(3):
        username=input('请输入用户名:')
        password=input('请输入用户密码:')
        if username=='sunxiangyang' and password=='123':
    
            print('欢迎{}回来'.format(username))
            break
        elif i <2:
            print('密码错误请重新输入，您还有{}次机会'.format(2-i))
        else:
            print('账户密码错误次数过多请稍后再试')'''
for i in range(0,50,1):
    print('*********',i)