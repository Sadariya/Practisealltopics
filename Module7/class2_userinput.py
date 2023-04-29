class student:
    stid=0
    stnm=''

    def getdata(self):
        # Restrict attributes of method
        self.__stid=input("Enter ID:")
        self.__stnm=input("Enter Name:")

    def printdata(self):
        print("Student ID:",self.__stid)
        print("Student Name:",self.__stnm)

st=student()
st.getdata()
st.printdata()