m,n=map(int,input().split())
for a in range(m+1,n):
  if a>1:
    for l in range(2,a):
      if(a%l==0):
        break
    else:
      print(a,end=' ')
