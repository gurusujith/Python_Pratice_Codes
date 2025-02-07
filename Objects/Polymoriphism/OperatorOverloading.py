class Demo1:
    def displ(self):
        print('Inside disp1')
    def __str__(self):
        return "Hello"
    def __add__(self,other):
        self.a = 20
        other.a =30
        return self.a+other.a   
class Demo2:
    def disp2(self):
        print("INSIDE disp2")
    def __str__(self):
        return 'Hi'
d1 = Demo1()
d2 = Demo2() 

print(d1) 
print(d2) 
print(d1+d2)


'''
In python if we print reference varaiable then it will 
display string representation of an address of an object
'''

'''
In python if we print reference varaiable then internally python
will invoke__str()__ which always returns string representation of an address of an object

--> In the above examples we have overridden __str__ methods in their respective classes.
'''


