'''
#ASSIGNMENT AS ON 11 APRIL 2019

1.Had to open a file and repalce the last word of the file with someother word. 

How to replace the last word. This is going to be using file handling

'''

"""
fileOpen = open("test.txt",'w')

writeInFile = fileOpen.write("This is all about overwriting the old file with the new one.")
fileOpen.close()
result = open("test.txt","r",encoding="utf-8")

print(result.read(1))
"""

listsSpace = []

with open("test.txt") as testFile:
    for line in testFile:
        for chars in line:
            if chars == " ":
                listsSpace.append(chars)
            print(chars[:10:])

print(" The total number of white spaces in the test file is",len(listsSpace))





