#Empty list
'''
Lists = []
print(Lists)

# List of numbers

Lists1 = [1,2,4,5]
print(Lists1)

#List of strings

Lists2 =['red','green']
print(Lists2)

#Multi dimensional List
#Nested list

Lists3 = [1,2,3,[4,5]]
print(Lists3)

# Mixed type of values
Trueef = True
Lists4 = [1,2,'ak','ud','vk',Trueef]
print(Lists4)

#using append

Lists5 = []
Lists5.append(1)
Lists5.append(False)
Lists5.append('ak')
print(Lists5)


#for loop append

Lists6 = []
for i in range(1,5):
    Lists6.append(i)
print(Lists6)

#x = input(" Enter a name to add to a list ?")

lists7 =  ['ak','ud','remo']
for words in lists7:
    print(words)


# Adding a tuple to a list
tupleValue = (1,2)
addTuple = Lists5.append(tupleValue)
print(Lists5)

# Adding a list to list


first = ['ak','vk','remo']
second = [1,3,5]
first.append(second)
print(first)
print(first[3])


my_list = ['geeks', 'for', 'geeks'] 
another_list = [6, 0, 4, 1] 
my_list.append(another_list) 
print(my_list)


#insert method

my_list = ['geeks', 'for', 'geeks'] 
my_list.insert(-2,'ak')
my_list.append('pk')
print(my_list)

#adding a value to particular position using insert

#extend

sampleList = [1,2,4]
secondList = [4,6,7]
sampleList.extend(secondList)
print(sampleList)
print(sampleList[4])
'''
#Indexing


#Negative indexing

lists = ['ak','vk','pk','rk','sk']
print(lists[-3::-1]) # start #stop # step
