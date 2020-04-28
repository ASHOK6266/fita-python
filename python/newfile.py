''''
l = range(0,10,2)

print(l)

for i in l:
    print(i)

copy
'''




def checkCaps(text):
    for i in text:
        if i.isupper():
            return True
        elif i == "":
            return True
        else:
            return False 

print(checkCaps("ALL IS WELL"))
print(checkCaps("Hi"))
print(checkCaps("   "))
print(checkCaps("dhgzx"))