n,k = map(int,input().split())
count = 0
for i in range(k,n+2):
    count += i*(n-i+1)+1
    count %=(10**9+7)
print(count)
