a=input()
a=a.lower()
v=("aeiou")
x=("bcdfghjklmnpqrstvwxyz")
if(a in v):
  print("Vowel")
elif(a in x):
  print("Consonant")
else:
  print("invalid")
