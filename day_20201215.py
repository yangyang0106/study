# a = [7,3,4,9,10,3,12,3,17]
# print(a.pop())
# print(a.pop(0))
# print(a.remove(3))
# del a[:2]
# print(a)

# a= [1,2,3]
# a.insert(1,4)
# print(a)
# a.append(10)
# print(a)
# a.extend([20,30])
# print(a)

mylist =  [58,5,68,17,65,621,45]
for i in range(len(mylist)-1):
    for j in range(0,len(mylist)-1-i):
        if mylist[j] > mylist[j+1]:
            # tmp = mylist[j]
            # mylist[j] = mylist[j+1]
            # mylist[j+1] = tmp
            mylist[j],mylist[j+1] = mylist[j+1],mylist[j]
print(mylist)