m=int(input())
n=list(map(int,input().split()))
n.sort()
med=n[int(m/2)]
print(med)
