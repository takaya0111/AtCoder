from itertools import combinations_with_replacement
n,m,q=map(int,input().split())
a = [0]*q
b = [0]*q
c = [0]*q
d = [0]*q
for i in range(q):
    a[i],b[i],c[i],d[i] = (map(int,input().split())) 

score=0
for A in combinations_with_replacement(range(1,m+1),n):
    s = 0
    for j in range(q):
        if A[b[j]-1]-A[a[j]-1]==c[j]:
            s+=d[j]
    score = max(score,s)
print(score)
