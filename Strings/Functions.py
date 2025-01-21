#without input and without return statement.
def add():
    a = 10
    b = 20
    print(f'Addition of {a} and {b} is: {a+b}')

#with input and without return statement
def sub(a,b):
    print('Subtraction:',a-b)

#without input and with return statement
def mul():
    return 10*20

# with input and with return statement
def div(a,b):
    return a/b

add()
sub(20,10)
print(mul())
print(div(20,10))