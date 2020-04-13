"""
#ASSIGNMENT AS ON 11 APRIL 2019

1.Had to open a file and repalce the last word of the file with someother word. 

How to replace the last word. This is going to be using file handling

fileOpen = open("test.txt",'w')

writeInFile = fileOpen.write("This is all about overwriting the old file with the new one.")
fileOpen.close()
result = open("test.txt","r",encoding="utf-8")

print(result.read(1))



listsSpace = []

with open("test.txt") as testFile:
    for line in testFile:
        for chars in line:
            if chars == " ":
                listsSpace.append(chars)

print(" The total number of white spaces in the test file is",len(listsSpace))



Using the list comprehension print either even index or odd index from a sentence



sampleInput = input(" Enter a sample sentence to retrieve only the even index :")

#print(type(sampleInput))

#LIST COMPREHENSION

result = [ sampleInput[x] for x in range(0,len(sampleInput)) if x%2 == 0 ]
print(result)

#ASSIGNMENT AS ON 11 APRIL 2019

Using lambda function from lists retrieve the words that starts with a

"""

lists = ['ak','dk','vk','ud','sd','rv','ana']
#lists = [2,4,6,7,9]

value  = list(filter(lambda x: (x[0] == 'a'), lists))

print(value)

