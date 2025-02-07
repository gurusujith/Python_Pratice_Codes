li = [10,5,3,20]
li.sort() # sort method won't return anything.
print(li) # [3, 5, 10, 20]

li2 = [10,5,3,20]
li.sort(reverse=True)
print(li2) # [20, 10, 5, 3]

li3 = [100,30,500,10]
sort_li3 = sorted(li3) # sorted method will return a new list.
print(sort_li3) # [10, 30, 100, 500]