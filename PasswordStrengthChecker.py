password=str(input("enter your password:"))
if len(password)>=6:
    if "#" in password or "&" in password:
        print("strong password")
else:
    print("weak password")    