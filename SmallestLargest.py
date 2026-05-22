largest=None
smallest=None
count=0

while True:
    n=int(input("enter the numbers:"))
    if n==0:
        break
    count +=1
    if largest is None or n>largest:
        largest=n
    if smallest is None or n<smallest:
        smallest=n
print("largest number is:",largest)
print("smallest number is:",smallest)
print("total numbers entered:",count)        
    
            
    
