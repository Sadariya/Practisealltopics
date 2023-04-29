'''class : it is collections of data member and member function in python using class keyword 
we can define the class'''

class student:
    # By default data members is public
    stid=12
    stnm='Sanket'

    def __init__(self) -> None:
        print ("this is default constructor")

    def getdata(self):
        print("This is Student Class.")
    
    def getsum(self,a,b):
        print("Sum:",a+b)


# Object of class
st=student()

# data member calling
print(st.stid)
print(st.stnm)

# member function calling
st.getdata()
st.getsum(23,43)