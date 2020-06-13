n,k = map(int,input().split())
d = []
for i in range(k):
    a = int(input())
    d.append((map(int, input().split())))
# print(d)
have = [-1]*n
# print(have[n-1])
for i in d:
    for j in i:
        # print(have[j-1])

        have[j-1]+=1

ans=0
for i in range(n):
    if have[i]==-1:
        ans +=1
print(ans)