
def factorial(number):
     return 1 if(number ==0 or number ==1) else(number * factorial(number-1))

number = int(input("Enter a number : "))
print("Factorial of",number,"is",factorial(number))