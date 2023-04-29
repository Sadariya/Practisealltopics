x=lambda a,b:a+b

print(x(56,89))

def getsum():
    print(x(56,89))

getsum()

y = lambda a,b,c :a*b*c

print (y(12,12,12))

x = lambda a,b : a*b

for i in range (20):

    a = i
    b = i

    print (f"{i} square is {x(a,b)}")