num = int(input("Enter a number: "))

sum_digits = 0
product = 1
temp = num

while temp > 0:
    digit = temp % 10
    sum_digits += digit
    product *= digit
    temp //= 10

if sum_digits == product:
    print("Spy Number")
else:
    print("Not a Spy Number")