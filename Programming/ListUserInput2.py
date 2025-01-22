li = input('Enter space seperated Elements') # 10 2 34 56 78
print(li)
li = li.split()
print(li) # ['10', '2', '34', '56', '78']
li = list(map(int, li))
print(li) # [10, 2, 34, 56, 78]


tup = tuple(map(int,(input('Enter space sperated elements').split())))
print(tup)

li = list(map(int,input().split())) # 10 2 34 56 78
print([i for i in li if i%2==0]) # [2, 34, 56, 78]