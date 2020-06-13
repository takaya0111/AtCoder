import itertools
n,x,y = map(int,input().split())
count = [0]*(n-1)
f = [[] for i in range(n)]
for i in range(n):
    if i==0:
        f[i].append(i+2)
    elif(i==n-1):
        f[i].append(i)
    else:
        f[i].append(i)
        f[i].append(i+2)

f[x-1].append(y)
f[y-1].append(x)
print(f)
a = set()
for i in range(n):
    a.add(i+1)

for A in  list(itertools.combinations(a,2)):
     k=0
     d = [A[0]]
     while True:
        for x in d:
            for i in f[x-1]:
                if i ==A[1]:  
                    count[k]+=1
                    break
            else:
                continue
            break
        else:
            k+=1
            d = []
            
            continue
        break

for i in range(n-1):
    print(count[i])