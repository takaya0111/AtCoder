n,a,b = map(int,input().split())
k = int(n/(a+b))
l = n%(a+b)
count = 0
count += k*a
if l>a:
    count +=a
else:
    count +=l

print(count)

