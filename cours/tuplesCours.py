# A empty tuple

empty_tuple = ()

# Tuple having an integer

tuple_integer = (1,2,45,55,43)
tuple_single = (1,)
print(type(tuple_single))
print(tuple_single)
# Tuple having mixed data types

tuple_mixed = (1,3,'stings',True,12.50)
tuple_list = (1,4,45,65,[23,45])
print(tuple_list)
# nested tuple
nested_tuple = (23,45,1,3,(45,True))
print(nested_tuple)

# Tuple created without a parenthesis

x = 23,45,64
print(type(x))

# unpacking a tuple
i,j,k = x
print(type(i))
print(j)

#Accessing tuple elements

tuple_integer = (1,2,45,55,43)
print(tuple_integer[2])
#print(tuple_integer[5])

#z = tuple_integer.append(85)
z = tuple_integer.pop(87)
#print(z)
# IndexError

#Index of a nested tuple
nested_tuple = (4,5,6,(6,7),4,5,3,7,4)
print(nested_tuple[3])

#Negative indexing

print(nested_tuple[-1])
print(nested_tuple[-3])

#Tuples slicing

print(nested_tuple[1::2])

#Tuples are immutable


#Concatenating two tuples

rv = 'aaa'
a = ('ak','sk',rv)
b = (True,14.5,'4')
c = a + b
print(type(b[2]))
#print(c)

x = '4'
y = ''

print(x+y)

###############################################################"""


tuples = ('i','a','i','o','u')

for vowels in tuples:
    if vowels == 'i' or vowels == 'a' or vowels == 'u':
        print('my name\'s first character is present in tuples ')
    else:
        print(False)
