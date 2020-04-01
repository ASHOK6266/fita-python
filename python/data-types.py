'''
The below example is for using a replace in-built function
Python3
'''

sampleString = "This is a string a and I am going to replace the white spaces with the hyphen"

print(sampleString.replace(" ","-"))

'''
The below is to check for palindrome
'''

string = "level"
var1 = string[:]
var2 = string[::-1]
#print(var2)
if(var1 == var2):
    print("The given variable is palindrome")
else:
    print("The variable is not a palindrome")