class Employee:
    empNumber : int
    __name : str
    __address : str
    __salary : float
    __jobTitle : str
    def __init__(self,empNumber,name,address,salary,jobTitle):
        self.empNumber = empNumber
        self.__name = name
        self.__address = address
        self.__salary = salary
        self.__jobTitle = jobTitle
    def getName(self):
        return self.__name
    def getAdress(self):
        return self.__address
    def setAdress(self,address):
        self.__address = address
    def getSalary(self):
        return self.__salary
    def getJobTitle(self):
        return self.__jobTitle
    def __del__(self):
        print("name of Employee " + self.__name + "has been deleted")
    def __str__(self):
        output = "Employee info \n .Emplyee number: "+ str(self.empNumber) + "\n .Name "+ self.__name + "\n .Address "+ self.__address + "\n .Salary" +str( self.__salary) + "\n .Job title " + self.__jobTitle
        return output
    
    def nonFormatedOutput(self):
        output = "Employee info  .Emplyee number: "+ str(self.empNumber) + " .Name "+ self.__name + " .Address "+ self.__address + " .Salary" +str( self.__salary) + ".Job title " + self.__jobTitle
Employee1 = Employee(1,"mohammad Khalid","amman jordan","500","consultant")
print(Employee1)
Employee1.setAdress("USA")
print(Employee1)
Employee2 = Employee(2,"Hala Rana","aqaba jordan","750","manager")
del Employee1
del Employee2