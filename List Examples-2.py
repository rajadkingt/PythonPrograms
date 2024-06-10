
list1=list(range(1,500,7))
print(list1)

''' clear a list'''
list1.clear()
print(list1)
list1=[1,2,2,2,3,4,5,6]

'''remove the first occurance of a value'''
list1.remove(2)
print(list1)
list1.remove(4)
print(list1)

list1.sort(reverse=True)
print(list1)

'''this will add the list but not its element'''
list2=[7,9,11,12]
list1.append(list2)
print(list1) #[6, 5, 3, 2, 2, 1, [7, 9, 11, 12]]

''' do this to add list elements to list1'''
list1.pop()
print(list1)
list1.extend(list2)
print(list1) #[6, 5, 3, 2, 2, 1, 7, 9, 11, 12]