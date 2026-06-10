num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:

    digit = num % 10

    reverse = reverse * 10 + digit

    num = num // 10

print("Reversed number:", reverse)

if reverse > original:
    print("Reversed is Bigger")

else:
    print("Original is Bigger or Equal")