rows = 5
col = 5
for i in range(rows):
    for j in range(col):
        if(i==0 or i==rows-1 or j==0 or j==col-1):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()