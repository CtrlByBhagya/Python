num=int(input("enter n:"))
result=0
fact=1
for i in range(1,num+1):
    fact=fact*i
    result=result+i/fact
    
print(result)