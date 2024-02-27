#Program to find a factorial of a number using Recursion

def recursion_fact(n):
    if n == 1:
        return n
    else:
        return n * recursion_fact(n-1)
    
num = int(input("Enter a num value : "))

if(num < 0):
    print(f"Factorial of a given number {num} is not possible")
elif(num == 0):
    print("Factorial of 0 is 1")
else:
    print(f"Factorial of a given number {num}  is = {recursion_fact(num)} ")