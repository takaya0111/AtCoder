n = int(input())
a = list(map(int,input().split()))
b= 1
c = 0
if min(a)==0:
    print(0)
else:
    for i in range(n):
        b *=a[i]
        if b>10**18:
            print(-1)
            c =1
            break
    if c ==0:
        print(b)