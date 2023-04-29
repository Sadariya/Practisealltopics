'''import re

mystr="This is Python!"

x=re.findall('is',mystr)

print(x)

if x: #true
    print("Success!")
else:
    print("Error!")
'''


import re

mystr="This is Python!5466"

x=re.findall('[A-Z]',mystr)
print ('A-Z Character :- ',x)
x=re.findall('[a-z]',mystr)
print ('a-z Character :- ',x)
x=re.findall('[A-Za-z]',mystr)
print ('A-Za-z Character :- ',x)
x=re.findall('[0-9]',mystr)
print ('0-9 Character :- ',x)
x=re.findall('[A-Za-z0-9]',mystr)
print ('A-Za-z0-9 Character :- ',x)
x=re.findall('^T',mystr)
print ('^T Character :- ',x)
x=re.findall('66$',mystr)
print ('66$ Character :- ',x)
x=re.findall('^[A-Z]',mystr)
print ('^[A-Z] Character :- ',x)
x=re.findall('[^A-Z]',mystr)
print ('[^A-Z] Character :- ',x)
x=re.findall('\w',mystr)
print ('\w Character :- ',x)
x=re.findall('\W',mystr)
print ('\W Character :- ',x)
x=re.findall('\s',mystr)
print ('\s Character :- ',x)
x=re.findall('\S',mystr)
print ('\S Character :- ',x)
x=re.findall('\d',mystr)
print ('\d Character :- ',x)
x=re.findall('\D',mystr)
print ('\D Character :- ',x)
x=re.findall('\AT',mystr)
print ('\At Character :- ',x)
x=re.findall('66\Z',mystr)
print ('66\Z haracter :- ',x)
x=re.findall('Py..on',mystr)
print ('py..on Character :- ',x)
x=re.findall('This|That',mystr)
print ('This|That Character :- ',x)
x=re.findall('[A-Z]|[a-z]',mystr)
print ('[A-Z]|[a-z] Character :- ',x)