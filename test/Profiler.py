arr1=[1,2,3]
arr2=[3,4,5]
filter1=lambda x: x in arr2
k = [x for x in [y for y in arr1 if filter1(y)]]
print(k)