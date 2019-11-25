class Employee:
    empNumber : int
    name : str
    address : str
    salary : float
    jobTitle : str
    def __init__(self,empNumber,name,address,salary,jobTitle):
        self.empNumber = empNumber
        self.name = name
        self.address = address
        self.salary = salary
        self.jobTitle = jobTitle
    def getName(self):
        return self.name
    def getAdress(self):
        return self.address
    def setAdress(self,address):
        self.address = address
    def getSalary(self):
        return self.salary
    def getJobTitle(self):
        return self.jobTitle
    def __del__(self):
        print("name of Employee " + self.name + "has been deleted")
    def __str__(self):
        output = "Employee info \n .Emplyee number: "+ str(self.empNumber) + "\n .Name "+ self.name + "\n .Address "+ self.address + "\n .Salary" +str( self.salary) + "\n .Job title " + self.jobTitle
        return output
    def nonFormatedOutput(self):
        output = "Employee info  .Emplyee number: "+ str(self.empNumber) + " .Name "+ self.name + " .Address "+ self.address + " .Salary" +str( self.salary) + ".Job title " + self.jobTitle
Employee1 = Employee(1,"mohammad Khalid","amman jordan","500","consultant")
print(Employee1)
Employee1.setAdress("USA")
print(Employee1)
Employee2 = Employee(2,"Hala Rana","aqaba jordan","750","manager")
