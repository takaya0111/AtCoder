k,n = map(int,input().split())
a =list(map(int,input().split()))
kyori = [0]*n
# print(a)
for i in range(1,n):
    # print(i)
    kyori[i]=a[i]-a[i-1]
kyori[0]=a[0]+(k-a[n-1])
print(k-max(kyori))
