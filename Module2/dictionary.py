stdata={'id':1,'name':'sanket','age':30}

# print(stdata)
# print(stdata['age'])
# print(stdata.get('name'))
# print(len(stdata))

'''stdata['id']=2
stdata['name']='mitesh'
print(stdata)
'''
# ------------------------------------- #

"""if 'name' in stdata:
    print("Yes....")
else:
    print("Nooo")"""

"""print(stdata.keys())
print(stdata.values())
if 'sanket' in stdata.values():
    print("Yes...")
else:
    print("Nooo")"""

# --------------------------------------------- #

# print(stdata)

"""for i in stdata:
    print(i)"""

"""for i in stdata.values():
    print(i)"""

"""for i in stdata.items():
    print(i)"""

stdata['sub']='Python'
# stdata.pop('id')
#del stdata['name']
#stdata.clear()
#del stdata
print(stdata)


stdata={'id':1,'name':'sanket','age':30}


stdata['Number'] = 7894561235

print (stdata)

# stdata.pop('Number')

# print (stdata)

stdata['Number'] = 456789152156

print (stdata)

# stdata.clear()

del stdata['name']

print (stdata)

list1 = ['name', 'Age', 'Subject' , 'Number']
list2 = ['Jay', 24, 'Python']

final_dict = dict(zip(list1,list2))

print (final_dict)