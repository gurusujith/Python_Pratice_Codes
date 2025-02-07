'''
s = 'kodnest'
print(s.isalnum()) # True   
print('kodnest12*'.isalnum()) #False
print('kodnest'.isalnum()) #True

print('kodnest12'.isalpha()) #false
print('code'.isalpha()) # True

print('12'.isdigit()) # True

print('apple'.islower()) # True
print('apple'.isuper()) # False

print(any([True,False,False])) # True
print(any([False,False,False])) # False

print(all([True,True,True])) # True
print(all([True,False,True])) # False
'''

s = input() #qA1
print(any([ i.isalnum() for i in s])) 
print(any([ i.isalpha() for i in s]))
print(any([ i.isdigit() for i in s]))
print(any([ i.islower() for i in s]))
print(any([ i.isupper() for i in s]))
