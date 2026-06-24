num = int(input("Enter a number: "))

square = num * num

rev = int(str(num)[::-1])
rev_square = rev * rev

if str(square)[::-1] == str(rev_square):
    print("Adam Number")
else:
    print("Not an Adam Number")