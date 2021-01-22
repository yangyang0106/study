# s='basdhbshjbdyuHJBSHJSBjhbhjvVgVKJKJNkjnlkNJJKNLnkmnkjnJHNJHKJKMJKLjnjn'
# print(len(s))
# code = ''
# import random
# ran = random.randint(0,len(s)-1)
# for i in range(4):
#     ran =random.randint(0,len(s)-1)
#     code += s[ran]
#
# print("验证码" + code)
#
# user_input = input("请输入验证码:")
# if user_input.lower() == code.lower():
#     print("验证码输入正确")
# else:
#     print("验证码输入错误")

# s1 = 'index lucy lucky goodrs'
# result = 'r' in s1
# print(result)
#
# position = s1.find('r')
# print(position)
#
# position = s1.find('1')
# print(position)
#
# s1.find('1')

# msg = '好好学习'
# print(msg)
# print('$$$$$$$$$$$$$$$$$')
# result = msg.encode('utf-8')
# print(result)
# print('######################')
# m = result.decode('utf-8')
# print(m)


# path = input('请选择文件：')  #C:\Users\sunxiangyang\Pictures\3333.jpg
# p = path.rfind('\\')
# filename = path[p+1:]
# print(filename)
# if filename.endswith('jpg') or filename.endswith('png') or filename.endswith('gif') or filename.endswith('bmp'):
#     print("上传文件成功")
# else:
#     print("文件格式不正确")
#

s1 = input('请输入第一个字符串:')
s2 = input('请输入第二个字符串:')
# s3 = ''
# for i in s1:
#     if i not in s2:
#         s3 = i
#         print(s3)
# s1 = s3
# print(s1)

#
# for i in s2:
#     s1 = s1.replace(i,'')
#     print(s1)