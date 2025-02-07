from abc import ABC, abstractmethod
class Demo1(ABC):
    pass
    
d1 = Demo1()


'''
If abstract class doesn't have any method then 
object for that abstract class can be created.
'''

class Demo2(ABC):
    def disp2(self):
        print('Inside disp2')
d2 = Demo2()
d2.disp2()
'''
If abstract class have only concrete method then object 
for that abstract class can be created and concrete.
'''

class Demo3(ABC):
    def info(self):
        print('Inside info')
    @abstractmethod
    def disp3(self):
        print('Inside disc3')

class Demo4(Demo3):
    pass

d4 = Demo4()
d4.info()
'''

'''
