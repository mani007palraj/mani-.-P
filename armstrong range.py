a,b=map(int,input().split())
for z in range(a+1,b):
  sum =0
  temp =z
  while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
  if z==sum:
    print(z,end=' ')
