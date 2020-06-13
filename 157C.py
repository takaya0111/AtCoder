from operator import itemgetter
n,m = map(int,input().split())
t = [list(map(int,input().split())) for _ in range(m)]
t.sort(key=itemgetter(0))
c = [i[1] for i in t ]
s = [i[0] for i in t]
# print(c)
x = 0

ans = "a"*n
ans = list(ans)
for i in range(n):
    for j in range(len(s)):
        if i==s[j]-1 :
            if str(c[j])!=ans[i] and ans[i]=="a":
                ans[i]=str(c[j])
            elif  str(c[j])!=ans[i] and ans[i]!="a":
                x =1
# print(ans)

if ans[0]=="0" and n!=1:
    x=1
for i in range(len(ans)):
    if ans[i]=="a":
        ans[i]="0"
# print(ans)
if ans[0]=="0"and n!=1:
    ans[0]="1"
if x==0:
    print(int("".join(ans)))
else:
    print(-1)

# if x==1:
#     print(-1)
# elif n!=1 and ans[3-n]=="0":
#     print(-1)
# elif m==0 and n!=1:
#     print(-1)
# elif m==0 and n==1:
#     print(0)
# else:
#     if ans[3-n]=="a" and max(s)<n and n!=1:
#         ans[3-n]="1"
#     # print(ans)
#     for i in range(3):
#         if ans[i]=="a":
#             ans[i]="0"
#     # if ans[n-1]=="0" and max(s)<n and n!=1:
#     #     ans[n-1]="1"
#     # print(ans)
#     ans = int("".join(ans))
#     # if len(str(ans))>n:
#     #     print(-1)
#     # else:
#     print(ans)


