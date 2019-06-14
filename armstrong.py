z= int(input())
sum =0
temp =z
while (temp > 0):
   num = temp % 10
   sum+= num ** 3
   temp //= 10
if z==sum:
   print("yes")
else:
   print("no")
