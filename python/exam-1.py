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

sampleSentence = 'Hello! From this sentence I am going to find the number of consonants vowels white spaces and special characters!!!!'

i = 0

while i < len(sampleSentence):
    #print(sampleSentence[i])
    if sampleSentence[i] == 'aeiou':
        lists = []
        lists.append(i)
        print(lists)
    i += 1