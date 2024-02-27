#Progra to check whether a given number is armstrong or not

num = int(input("Enter the num value : "))
sum = 0

temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if num == sum:
    print(num,"is a armstrong number")
else:
    print(num,"is not armstrong number")