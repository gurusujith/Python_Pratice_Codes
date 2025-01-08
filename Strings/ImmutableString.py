'''Strings are immutable:
    1. Once we declare the String we can't modify it , if we try to modify the string 
     it will create new String.
    2. If new String does not have any reference variable then it will be removed.
    3. Python Internally uses string Interning.
    4. String Interning is the process of Checking String Intern pool 
    before creating any new object.
    5.Whenever we want to create new object, Python first will check String intern pool, weather that Object already exist or not.
    6. When object already exist in the String intern Records then Address of existing object will be reused'''
#s1 = 'Kodenst'
#s1 = s1.upper()
#print(s1)

#s1 = 'k'
#print(s1,id(s1))

s1 = 'Hello'
s2 = 'World'
print(s1,id(s1))
print(s2,id(s2))

print(s1[0])
print(s1[-1])

print('s1 ID of H:',id(s1[0]))
print('s1 ID of o:',id(s1[-1]))  

print('s2 ID of W:',id(s2[0]))
print('s2 ID of o:',id(s2[1]))

print('s1 Id of l:',id(s1[2]))
print('s1 Id of l:',id(s1[3]))
print('s2 Id of l:',id(s2[3]))