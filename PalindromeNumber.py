n=int(input("enter a number:"))
s=str (n) [::-1]
s=int(s)

if n==s:
    print("palindrome number")
else:
    print("not palindrome number")    