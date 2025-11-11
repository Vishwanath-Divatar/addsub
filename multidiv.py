#Simple Python program for multiplication and division of two numbers

#Take input from the user 
num1= float(input("Enter first number:"))
num2= float(input("Enter second number:"))

#Multiplication
multiplication = num1*num2

#Division (with check to avoid division by zero)
if num2 !=0:
    division = num1/num2
else:
    division = "undefined (cannot divide by zero)"
    
#Display results
print(f"\nMultiplication of {num1} and {num2}={multiplication}")
print(f"Division of {num1} by {num2} = {division}")