'''
1. Write a Python program to create a tuple.



tup1 = (51,55,67,65,98)


2. Write a Python program to create a tuple with different data types. Go to the editor



tup2 = (41,45.56,'ak','different data types',True)


3. Write a Python program to create a tuple with numbers and print one item. Go to the editor


tup3 = (1,3,5,'Hi, I am accessible via index value')

print(tup3[3])



4. Write a Python program to unpack a tuple in several variables.



x = ('ak',25,'web developper') # Tuple packing
(name,age,profession) = x # Tuple unpacking

print(name)
print(age)
print(profession)



5. Write a Python program to add an item in a tuple.


# AttributeError: 'tuple' object has no attribute 'append' (If we use append built in function then we get an attribute error in tuple)
tuplex = ('Hello','Adding a value to tuple',25)
tuplex1 = ('software engineer',)
concat = tuplex + tuplex1
print(concat)

# converting the tuple into lists and adding a value
changeAsList = list(concat)
changeAsList.append('interested in python scripts')
print(changeAsList)

6. Write a Python program to convert a tuple to a string. Go to the editor

'''

tuples = ('1','2','5')

result = str(tuples)
print(type(result))
