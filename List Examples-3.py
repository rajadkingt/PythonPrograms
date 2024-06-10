list1=list(range(1,25))
sqr=lambda x:x*x
for i in list1:
    print('{}->{}'.format(i,sqr(i)))

print([x*x for x in list1])   
