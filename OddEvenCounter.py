even=0
odd=0

for i in range(5):
    num=int(input("enter a number:"))
    if num%2==0:
        even+=1
    else:
        odd+=1
print("number of even numbers:",even)
print("number od odd numbers:",odd)
            
