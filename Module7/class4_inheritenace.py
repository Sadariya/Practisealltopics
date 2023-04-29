'''class student:
    @staticmethod
    def getdata():
        print("This is getdata.")
    @staticmethod   
    def showdata ():
        print ("This is showdata method")
    

st=student()
st.getdata()
st.showdata()'''

# Single Level Inheritence : one class contain the property of other class.

'''class father:
    # data member 
    car=0
    bal=0
    # member function
    def getdata(self):
        self.car=input("Enter Car details:")
        self.bal=input("Enter Bank Balance details:")

class son(father):
    def printdata(self):
        print("Total car:",self.car)
        print("Total Bank Balance:",self.bal)

sn=son()
sn.getdata()
sn.printdata()'''

# multiple Inheritence : one class contain the prorety of multiple class in it .

'''
class ashok:
    aid=0
    asub=''

    def __agetdata(self):
        self.aid=input("Enter Ashok's ID:")
        self.asub=input("Enter Ashok's Subject:")
    def showdata (self):
        self.__agetdata()

class nirav:
    nid=0
    nsub=''

    def n_getdata(self):
        self.nid=input("Enter Nirav's ID:")
        self.nsub=input("Enter Nirav's Subject:")

class hitesh:
    hid=0
    hsub=''

    def h_getdata(self):
        self.hid=input("Enter Hitesh's ID:")
        self.hsub=input("Enter Hitesh's Subject:")

class tops(ashok,nirav,hitesh):
    
    def printdata(self):
        print("-------Ashok's Data-------")
        print("Ashok's ID:",self.aid)
        print("Ashok's Subject:",self.asub)
        print("-------Nirav's Data-------")
        print("Nirav's ID:",self.nid)
        print("Nirav's Subject:",self.nsub)
        print("-------Hitesh's Data-------")
        print("Hitesh's ID:",self.hid)
        print("Hitesh's Subject:",self.hsub)


tp=tops()
tp.showdata()
tp.n_getdata()
tp.h_getdata()
tp.printdata()
'''
# Multi-level Inheritence :-

'''class grandfather:
    house=0
    gold=0

    def g_getdata(self):
        self.__house=input("Enter House details:")
        self.__gold=input("Enter Gold details:")
        
        self.house = self.__house
        self.gold = self.__gold

class father(grandfather):
    car=0
    bal=0

    def f_getdata(self):
        self.car=input("Enter Car details:")
        self.bal=input("Enter Bank balance details:")

class son(father):
    def printdata(self):
        print("------Grandfather's Data------")
        print("House:",self.house)
        print("Gold:",self.gold)
        print("------Father's Data------")
        print("Car:",self.car)
        print("Bank Balance:",self.bal)

sn=son()
sn.g_getdata()
sn.f_getdata()
sn.printdata()'''