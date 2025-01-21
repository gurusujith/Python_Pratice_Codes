'''
1.Conditional Statements : if, elif, else
2. Looping Statements : for, while
3. Control/Jumping Statements : break, continue, pass
'''

def checkAge(age):
    if age >= 18:
        print("You are eligible to vote")
    else:
        print("You are not eligible to vote")
checkAge(20)

#WAP to display 'Child' if age is below 18, display 'Adult' is age is above 18.
#display senoir citizen if age is above 65.
def displayAgeCateg(age):
    if age < 18:
        print("Child")
    elif age > 18 and age < 65:
        print("Adult")
    elif age >= 65:
        print("Senior Citizen")
    else:
        print("Invalid Age")
displayAgeCateg(int(input("Enter your age: ")))

