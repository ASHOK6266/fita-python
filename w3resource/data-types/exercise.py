'''
14. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'bad' follows the 'poor', 
replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
Sample String : 'The lyrics is not that poor!'
Expected Result : 'The lyrics is good!'

sampleString = 'The lyrics is not that poor!'

notString = sampleString.find('not')
poorString = sampleString.find('poor')

sampleString.replace('not','good')
print(sampleString)

12. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'

'''



sampleString = 'abc', 'xyz'
changeDatatype = list(sampleString)

changeDatatype.replace(", ", " ")

print(changeDatatype)



