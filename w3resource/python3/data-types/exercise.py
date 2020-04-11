'''
14. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'bad' follows the 'poor', 
replace the whole 'not'...'poor' substring with 'good'. Return the resulting string. 
Sample String : 'The lyrics is not that poor!'
Expected Result : 'The lyrics is good!'


import re

sampleString = 'The lyrics is not that poor!'

find = re.findall("not",sampleString)

modifiedSentence = sampleString.replace(find,"good")

print(find)



13. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
If the given string is already ends with 'ing' then add 'ly' instead. If the string length of the given string 
is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'

'''

#sampleString = 'abc'
sampleString = 'following'

#slicing = sampleString[-3:]

if len(sampleString) >= 3:
    if sampleString[-3:] == 'ing':
        result = sampleString + 'ly'
        print(result)
    else:
        result = sampleString + 'ing'
        print(result)
else:
    pass
