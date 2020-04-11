'''
rengineering, backward propogation, reverse engineering


data = ('india', 'maldives', 'nepal', 'Bangaladesh', 'srilanka')

hit_request = ['Na','german', 'chile', 'Australia']

hit_not_allowed = ['pak','saudi','china']

dit = {}

hit_request.append('france')
hit_request.append('maldives')
hit_request.append('Italy')
hit_request.append('Na')
hit_request.append('china')
hit_request.append('saudi')

for i in hit_request:
    if i in data:
        data_msg = "Allow data to have a new API request"
        print(data_msg)
        dit[i] = data_msg
    elif i in hit_not_allowed:
        data_msg = "Request from these countries is not allowed"
        print(data_msg)
    else:
        data_msg = "Site not found/ 404 error"
        print(data_msg)
        dit[i] = data_msg

#print(dit)


# CREATE A FILE

new_file = open("test.md","w")

new_file.write("This is the readme file")

# READING A FILE

read_file = open("test.md","r")

result = read_file.read()
result1 = read_file.readlines()

#print(len(result))

i = 0

lists = []

#print(len(result))

while i < len(result):
    lists.append(result[i])
    i += 1

f = open("test.md","r+")
value = f.read().splitlines() # inbuilt function
print(len(value))

print(value[:293])

'''
s= 'my name is senthil'

#print(s[3])

i = 0

while i < len(s):
    if(s[i]%2)== 0:
        print(s[i])
    i += 1

