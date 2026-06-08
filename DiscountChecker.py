item1 = int(input("Enter price of item 1: "))
item2 = int(input("Enter price of item 2: "))
item3 = int(input("Enter price of item 3: "))

total = item1 + item2 + item3

print("Total bill:", total)

if total > 500:
    print("You get a discount!")
else:
    print("No discount.")