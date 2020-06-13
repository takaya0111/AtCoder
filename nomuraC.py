n = int(input())
a = list(map(int,input().split()))
if a[0] == 1 and n == 0:
    print(1)
    exit()
su = sum(a)
# print(su)
l = [su]*(n+1)
for i in range(1,n+1):
    l[i]=l[i-1]-a[i-1]
# print(l)
count=0
x = 0
m=[1]*(n+1)
for j in range(1,n+1):
    m[j] = m[j-1]*2
    if m[j]>l[j]:
        m[j]=l[j]
    if (m[j]<a[j])or(m[j]==a[j] and j!=n):
        # print(m[j],a[j])
        x = 1
        break
    # print(m[j])
    count += m[j]
    m[j] -= a[j]
count+=1

if x==1 or a[0]!=0 :
    print(-1)
else:
    print(count)