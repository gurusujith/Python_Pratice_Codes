# rverse() will reverse the original object.
li = [10,5,20,7,40]
print('Before Reverse:',li) # [10, 5, 20, 7, 40]
li.reverse()
print('After Reverse:',li) # [40, 7, 20, 5, 10] 

#reversed(object) will return the reversed object(iterable_object).
li2 = [11,6,8,22]
reverse_li2 = list(reversed(li2))
print(li2) # [11, 6, 8, 22]
print(reverse_li2) # [22, 8, 6, 11]

li3 = [1,5,2,9]
new_list = list(reversed(li3)) # [9, 2, 5, 1] --> creating new reversed list
li3.reverse() # --> reversing original list