b=int(input())
temp=b
rev=0
while(b>0):
    dig=b%10
    rev=rev*10+dig
    b=b//10
if(temp==rev):
    print("yes")
else:
    print("no")
