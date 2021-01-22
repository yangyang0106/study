import random
import os
import json
recode = None
if os.path.exists('赌狗之家巅峰榜榜.json'):
    with open('赌狗之家巅峰榜榜.json', 'r', encoding='utf-8') as f:
        recode = json.load(f)
else:
    recode = {}
    with open('赌狗之家巅峰榜榜.json', 'w', encoding='utf-8') as f:
        json.dump(recode,f)



guess_count = 0
print('*'*10,'欢迎进入赌狗之家','*'*10)
if recode.keys() is None:
    min_v = min(recode.items(), key=lambda x: x[1])
    for k, v in recode.items():
        if v ==  min_v[1]:
            print('现在最牛逼的人物是%s' % k)
            break

username=input('请输入赌狗账户名:')
#password=input('请输入密码：')
money = int(input('请告诉我你带了多少钱:'))
# if username=='sxy' and password == '123' and money>=0:
#     print('欢迎来到赌狗之家')
print('每局游戏两块大洋')
ran_num= random.randint(0,1000)
print('-'*10,'游戏开始','-'*10)
while (True):
    guess_count += 1
    conjecture = input('请输入你要猜测的值:')
    if int(money) <= 0:
        print('金钱用完请重新充值！')
        break
    elif int(conjecture) == ran_num:
        money +=8
        print('恭喜你猜对了')
        print(money)
        recode[username] = guess_count
        min_v = min(recode.items(),key=lambda x:x[1])
        for k,v in recode.items():
            if guess_count < min_v[1]:
                print('恭喜你，进入了巅峰榜')
                break
        else:
            print('你只是个菜狗')
        with open('赌狗之家巅峰榜榜.json', 'w', encoding='utf-8') as f:
            json.dump(recode, f)
        break
    elif int(conjecture) < ran_num:
        money -=2
        print('你猜小了，请重新猜测')
    else:
        money -= 2
        print('你猜大了，请重新猜测')


