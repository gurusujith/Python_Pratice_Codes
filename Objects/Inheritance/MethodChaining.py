'''
Method Chaining: is the process of calling
one method from another method.
'''
class GrandParent:
    def cook(self):
        print("GrandParent can cook Biryani")
class Parent(GrandParent):
    def cook(self):
        print("Parent can cook Biryani and Pulav")
class Child(Parent):
    def cook(self):
        print("Child can't cook")
        super().cook() 
        super(Parent,self).cook() # Method Chaining
c = Child()
c.cook() 