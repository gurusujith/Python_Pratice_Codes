# map(function, iterable_object) -> Iterator Object
# map() function will return the iterator object, which can be converted to list, tuple, set, etc.

def double(x):
    return x*2

li = [1,2,3,4,5]
double(li) # [2, 4, 6, 8, 10]

# using map() function
double_li = list(map(double,li))
print(double_li) # [2, 4, 6, 8, 10]

# converting string to integer
tup = ('10','20','30','40') 
print(tup) # ('10', '20', '30', '40')
tup = tuple(map(int,tup)) 
print(tup) # (10, 20, 30, 40)

# converting string to float
li2 = [1,5,66]
new_li = list(map(float,li2))
print(new_li) # [1.0, 5.0, 66.0]