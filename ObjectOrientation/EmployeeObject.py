class Employee:
    company_name = 'code'
    def __init__(self,name,age,desigantion):
        self.name = name 
        self.age = age
        self.designation = desigantion
        
    def login(self,time):
         print(f'{self.name} logged in at {time}')

    def logout(self,time):
        print(f'{self.name} logged out at {time}')

    def work(self,hours):
        print(f'{self.name} worked for {hours}')

    def getDetails(self):
        print("Employee Name: ",self.name)
        print("Employee Age: ",self.age)
        print("Employee Designation: ",self.designation)

#Creating Objects:       
e1 = Employee("SK",22,"SDE")
e2 = Employee("Pk",24,"Manager")
e3 = Employee("Ak",23,"Developer")

e1.getDetails()
e2.getDetails()
e3.getDetails()

