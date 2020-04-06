'''
1. Write a Python program to create a set. 

# A set is created using the function set()

#An empty set
sets1 = ()

#A non-empty set
sets = set([1,2,3,4])

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

2. Write a Python program to iteration over sets. Go to the editor



days = set(["mon","tues","wed","thurs","fri","sat","sun"])

for d in days:
    print(d)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

3. Write a Python program to add member(s) in a set.

num = set([1,2,3,4,5,6])
num.add(7)
print(num)
print(type(num))

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

4. Write a Python program to remove item(s) from set.


days = set(["mon","tues","wed","thurs","fri","sat","sun"])
days.discard("sun")
print(days)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
5. Write a Python program to remove an item from a set if it is present in the set.


numbers = set([1,2,4,5,3,6])

inputNumber = int(input("Enter a number to remove from the list "))

if inputNumber in numbers:
    numbers.discard(inputNumber)
    print("Number removed from the list")
else:
    print(" The number is not present in the set")

print(numbers)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

6. Write a Python program to create an intersection of sets.

color = set(["red","green","violet","white"])
rainbow = set(["red","orange","yellow","green","blue","indigo","violet"])
thirdColor = set(["white","red"])

intersect = color.intersection(rainbow)
intersect2 = color.intersection(rainbow,thirdColor)
print(intersect)
print(intersect2)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

7. Write a Python program to create a union of sets. Go to the editor


8. Write a Python program to create sets difference. Go to the editor

a = set([1,2,3,4,5])
b = set([3,4,5])
print(a-b)
print(b-a)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

9. Write a Python program to create a symmetric difference. Go to the editor

'''






























