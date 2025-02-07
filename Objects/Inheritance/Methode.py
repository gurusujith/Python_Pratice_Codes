class Student:
    def cook(self):
        print("Student is cooking")
    def paly(self):
        print("Student is playing")
    
class Employee(Student):
    def work(self):
        print("Employee is working")
    def cook(self):
        print("Employee is cooking")
        super().cook()
        super(Student,self).cook()
e = Employee()
e.play()

'''
work() :Specialized method : only in child  class
play() :Inherited method : used as it is child class
cook() : Overridden method : change implementation  in child class   
'''
