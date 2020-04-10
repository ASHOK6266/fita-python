'''

A dictionaries that contains multiple students details (id,fname,lname,blood group)
When I enter the name (if the there is same fname ask them for lname) give the id,fname, last name, blood group
Sample data : 
{'101':['Ram','Navin','o+ve'],'102':['Sheela','Ramanujam','B+ve','103':['Ram','shankar','B+ve'],'104':['Rohini','Mittal','B+ve'],'105':['shankari','Raju','B-ve']}


sampleData = {'101':['Ram','Navin','o+ve'],'102':['Sheela','Ramanujam','B+ve'],'103':['Ram','shankar','B+ve'],'104':['Rohini','Mittal','B+ve'],'105':['shankari','Raju','B-ve']}



x = input(" Enter the first name ?")
#y = input(" Enter the last name ?")

dicts = {}

for i in sampleData:
    if sampleData[i][0] == x:
        dicts.update({i:sampleData[i]})
        
print(dicts)



2. From a sentence find the number of vowels,special characters,consonants and number of spaces.

'''

sampleSentence = ' GeeksforGeEks !!!'

i = 0

vowelCheck = set('aeiouAEIOU')
specialCharacters = set('!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~')

listsVowels = []
listsSpace = []
listsCharacters = []

while i < len(sampleSentence):
    print(sampleSentence[i])
    if sampleSentence[i] in vowelCheck:
        listsVowels.append(sampleSentence[i])
    elif sampleSentence[i] == " ":
        listsSpace.append(sampleSentence[i])
    elif sampleSentence[i] in specialCharacters:
        listsCharacters.append(sampleSentence[i])
    
    i +=1
    
print("Number of vowels in sample sentence is ",len(listsVowels))
print("Number of white space in sample sentence is ",len(listsSpace))
print("Number of special characters in sample sentence is ",len(listsCharacters))

