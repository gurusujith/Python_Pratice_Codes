'''
for control_variable in Iterable_object:
'''
for i in 'kodnest':
    print(i)

for j in [10,20,30]:
    print(j+5)

for num in range(1,11):
    print(num,end=' ')
print('')

for num in range(11,21,2):
    print(num,end=' ')
print('')

for i in range(5):
    print(i,end=' ')
print('')

# WAP to print all even numbers from 1-10
for num in range(1,11):
    if (num % 2 == 0):
        print(num,end=' ')
print('')

i=0
while(i<10):
    print(i+100)
    i = i+1

# WAP to print the numbers from 1-10 but if number i 6 then skip printing
for i in range(1,11):
    if (i == 6):
        continue
    print(i,end=' ')

# WAP to print number from 1-10 but if numberr if 5 then stop printing
for i in range(1,11):
    if(i==5):
        break
    print(i,end=' ')

for i in range(1,11):
    if(i==5):
        pass
    print(i,end=' ')


