name , *marks= "John", 90, 80, 70, 60
print(name)
print(marks)
# Output:   John    [90, 80, 70, 60]

# *marks will take all the values except the first and last value.
name, *marks,age =['Rahul',100,85,74,35] 
print(name)    # Rahul
print(marks)   # [100, 85, 74]
print(age) # 35
