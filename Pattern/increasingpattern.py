rows = 5
#Increasing pattern
for i in range(rows):
    for j in range(i+1):    #0+1 = 1, 1+1 = 2, 2+1 = 3, 3+1 = 4, 4+1 = 5
        print('*',end=' ')
    print()
#Decreasing pattern
for i in range(rows-1,0,-1):    #5-1 = 4 , 4-1 = 3, 3-1 = 2, 2-1 = 1
    for j in range(i):
        print('*',end=' ')
    print()