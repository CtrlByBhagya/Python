num = int(input("Enter a number: "))

i = 1

while i * i < num:
    i += 1

if i * i == num:
    print("Perfect Square")
else:
    print("Not a Perfect Square")