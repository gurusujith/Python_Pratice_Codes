'''
The variables which are public, can be accesses inside the same class,
outside of any class, inside the child class,inside non-child class.
'''

class Demo1:
    def __init__(self,name):
        self.firstname = name
    def disp1(self):
        print(self.firstname)
d1 = Demo1('Akash')
print(d1.firstname)
d1.disp1()

class Demo2(Demo1):
    def disp2(self):
        print(self.firstname)
d2 = Demo2('Pooja')
print(d2.firstname)
d2.disp2()

