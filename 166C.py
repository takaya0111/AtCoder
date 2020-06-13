n,m=map(int,input().split())
h = list(map(int,input().split()))
a = [list(map(int,input().split())) for j in range(m)]
# print("h:",h)
# print("a",a)
can_go = [[] for i in range(n)]
# print(can_go)
for i in a:
    # print(i)
    can_go[i[0]-1].append(i[1])
    can_go[i[1]-1].append(i[0])
# print(can_go)
b = 0
ans=0
for i,j in enumerate(can_go):
    # for j in can_go:
    b= 0

    for k in j:
        # print( h[k-1]-h[i])
        if h[k-1]>=h[i]:
            b=1
            # print("break")
            break
    if b==1:
        b=0
    else:
        ans+=1
print(ans)