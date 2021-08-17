#find a sum of natural numbers in a manual way
num=45
if num<0:
    print("Enter a positive number")
else:
    sum=0
    while(num>0):
        sum+=num
        num-=1
print("The sum is",sum)    
# find a natural numbers using a formula
num=29
if num<0:
    print("Enter a positive number")
else:
    sum=num*(num+1)
