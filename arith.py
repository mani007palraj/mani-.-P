w,x,y=map(int,input().split())
if(w>1 and w<=100000):
  z=int((w/2)*(2*x + (w-1)*y))
  print(z)
