'''

1. Write a Python program to sum all the items in a list.


list_values = [2,4,5,6]

index = 0
while index < len(list_values):
    print(list_values[index])
    index += 1


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

2. Write a Python program to multiplies all the items in a list. 



3. Write a Python program to get the largest number from a list.



lis = [2,7,8,89,78,98,87,34]
large = max(lis)
print(large)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


5. Write a Python program to count the number of strings where the string length is 2 or more 
and the first and last character are same from a given list of strings.


#HOW TO FIND THE LENGTH

sample =  ['abc', 'xyz', 'aba', '1221','1','121']  # x[0] = a

empty = []
#empty2 =[]

#empty2.extend()

for x in sample:
    if len(x) >= 2 and x[0] == x[-1]:
        empty.append(x)
        #empty2.extend(list(x)) # The return format will be in the form of list
print(len(empty)


7. Write a Python program to remove duplicates from a list

sampleList = ['1','ak','ak','1','5']


tup = ('1','2')
se = {'1','55','65'}
list1 = []
list2 = []
list1.extend(tup)
list1.extend(se)

# Always should use append
list2.append(tup) 

print(list2)

dict3 = {'as': 33, 'ak': 33, 'an': 33}


for k,v in dict3.items():
    #print(k)
    
print(dict3.values())

'''