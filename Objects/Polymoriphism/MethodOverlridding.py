'''
Polymorphism: It is a concept where a single task can be performed in different ways.
=> It is method overloading and method overriding.
=> It can be written duck typing.
'''
#Methodriding
#IN this code we are achieving Polymorphism by using Method Overriding.
class Calculator:
    def calculate(self,a,b):
        pass
class Add(Calculator):
    def calculate(self, a, b):
        print('Addition:',a+b)

class Sub(Calculator):
    def calculate(self,a,b):
        print('Subtraction:',a-b)
class Mul(Calculator):
    pass


ref = Add()
ref.calculate(10,20) # Addition: 30

ref = Sub()
ref.calculate(40,20) # Subtraction: 20

ref = Mul()
ref.calculate(10,20) # AttributeError: 'Mul' object has no attribute 'calculate'



'''
Duck Typing: It is a concept where the type or class of an object is less important than the methods it defines.
def permit(ref,a,b):
    if type(ref).__name__ == "Div":
        print("Div class does not have calculate method")
    else:
        ref.calculate(a,b)

permit(Add(),10,20) # Addition: 30
permit(Sub(),40,20) # Subtraction: 20
permit(Mul(),10,20) # Multiplication: 200
'''

'''
ref won't check the type of object.
ref on;y givvs importance to the calculate method.
ref  only gives importance to the methods of object.
'''
