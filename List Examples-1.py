'''List Examples'''

list1=list(range(1,10))
print(list1)

list1=list(range(0,10,2))
print(list1)

list1=list(range(0,30,3))
print(list1)

list2=list1
print(list2)

list1.pop()
print(list1,list2)

list2.pop()
print(list1,list2)
print(list1+list2)
print(list1>list2)
list2.append(100)
print(list1==list2)
print(list1,list2)