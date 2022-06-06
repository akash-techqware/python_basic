# List
list = [1,2,3]
print(list)

# Can be use with mixed datatypes

list1 = ["STRING", 100, 255.5]
print(list1)

# to check the length of list
list3 = ["String", 1000, 255.5]
print(len(list3))

# Slicing and Indexing in list
list4 = ['one', 'two', 'three']
print(list4[0])
print(list4[1])
print(list4[2])

# Slicing
print(list4[0:])
print(list4[1:])

# List Concatination
list5 = [1,2,3]
list6 = [4,5,6]
x = list5 + list6
print(x)

# To change or mutated one element in list
list6 = [1,2,3]
list6[0] = 'One'
list6[2] = 'Three'
print(list6)

# To append/add new item in the end of list
list7 = [1,2,3,4,5]
list7.append(6)
print(list7)

# To moving out item from list
list8 = [1,2,3,4,5]
list8.pop()
print(list8)

# To remove item from specific index
list9 = [1,2,3,4,5]
# list9.pop(0)
list9.pop(1)
print(list9)

# Sort and reverse in list
list10 = [5,3,2,1,4]
list10.sort()
x = list10
print(x)

# reverse in list
list11 = [5,3,2,1,4]
list11.reverse()
x = list11
print(x)

