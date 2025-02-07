# No inheritance is required in Duck Typing
#so there is no method overriding and method overloading.
class Add:
    def calaculator(self,a,b):
        print('Addition:',a+b)

class Sub:
    def calaculator(self,a,b):
        print('Subtraction:',a-b)

class Mul:
    pass


def permit(ref,a,b):
    if type(ref).__name__ == "Mul":
        print("Mul class does not have calculate()")
    else:
        ref.calaculator(a,b)

permit(Add(),10,20) # Addition: 30
permit(Sub(),40,20) # Subtraction: 20
permit(Mul(),10,20) # AttributeError: 'Mul' object has no attribute 'calaculator'   


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
