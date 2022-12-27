#Getting a input of the number from the user
num=int(input("Enter a number: "))
#Creating a variable for the factorial value
fact=1
a=1

#Code for getting the factorial of the number
while a <= num:
    fact*= a
    a+=1
#Printing the factorial value
print("The factorial of", num, "is", fact)
