d=int(input())
if(d%4==0 and d%100!=0):
  print('Yes')
elif(d%100==0):
  print('No')
elif(d%400==0):
  print ('Yes')   
 else:
   print('No')
