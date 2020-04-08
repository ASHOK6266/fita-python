'''
rengineering, backward propogation, reverse engineering

'''
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


