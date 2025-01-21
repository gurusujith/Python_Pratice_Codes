#If String is holding integer then it can be converted into int.

a = '30'
print(a,type(a))
b = int(a)
print(b,type(b))

#str to int conversion is not allowed.
x = 'Kod'
print(x,type(x))
#y = int(x)
#print(y,type(y))

p = float(input('Enter Float type data')) #12.22
print(p,type(p))

#bool
q = 10
print(q,type(q))
q = bool(q)
print(q,type(q))


'''
1. While converting int to bool for all non Zero values we will get true.
2. While converting int to bool for 0 and empty stringd we will get false.'''