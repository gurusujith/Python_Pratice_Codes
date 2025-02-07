class Student:
    def learn(self):
        print(self.name ,'is learning')
    def play():
        print('Inside play Method')

s1 = Student()
#s1.play() # TypeError: play() takes 0 positional arguments but 1 was given
s1.name = 'Pooja'
print('Name is',s1.name)
s1.learn() 


        