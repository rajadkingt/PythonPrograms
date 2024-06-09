'''List Examples'''

list1=list(range(1,10)) 
print(list1) #[1, 2, 3, 4, 5, 6, 7, 8, 9]

list1=list(range(0,10,2))
print(list1) #[0, 2, 4, 6, 8]

list1=list(range(0,30,3))
print(list1) #[0, 3, 6, 9, 12, 15, 18, 21, 24, 27]

list2=list1
print(list2)#[0, 3, 6, 9, 12, 15, 18, 21, 24, 27]

list1.pop()
''' Popping element in list1 also pops element in list2'''
''' This is called aliasing. Both list1 and list2 refer to same list object in memory'''
print(list1,list2)

list2.pop()
print(list1,list2)
print(list1+list2)
print(list1>list2)
list2.append(100)
print(list1==list2)
print(list1,list2)