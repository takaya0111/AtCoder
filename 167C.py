n,m,x = map(int,input().split())
book = [list(map(int, input().split())) for _ in range(n)]
cos_min=10**10*n
for i in range(1,2**n):
    s_c= [0]*(m+1)
    choose = bin(i)[2:].zfill(n)

    for j in range(n):
        if choose[n-j-1]=="1":  
            s_c = [a+b for (a,b)in zip(s_c,book[j])]

    for j in s_c[1:]:
        if j<x:
            break
    else:
        cos_min=min(cos_min,s_c[0])

if cos_min!=10**10*n :
    print(cos_min)
else:
    print(-1)    
