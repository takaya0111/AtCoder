n= int(input())
s = str(input())

r = set()
g = set()
b = set()
for i in range(n):
    if s[i]=="R":
        r.add(i)
    elif s[i]=="G":
        g.add(i)
    else:
        b.add(i)

score = len(r)*len(g)*len(b)
for i in r:
    for j in g:
        dist=abs(j-i)
        if (i>j):
            bi = i+dist
            if bi in b:
                score -=1
            bi = j-dist
            if bi in b:
                score -=1
        else:
            bi = j+dist
            if bi in b:
                score-=1
            bi = i-dist
            if bi in b:
                score-=1
        if((i+j)%2==0 and (i+j)/2 in b):
            score-=1
# print(count_)
print(score)
# for i in r:
#     for j in g:
#         if (i>j)and(2*i-j in b):
#             score-=1
#         if (i>j)and(2*j-i in b):
#             score-=1
#         if(j>i)and(2*j-i in b):
#             score-=1
#         if(j>i)and(2*i-j in b):
#             score-=1
#         if((i+j)/2 in b):
#             score-=1
# # print(count_)
# print(score)
# for i in range(n-2):
#     a = s[i]
#     for j in range(1,n-i):
#         if (a!=s[j+i]):
#             now = i+j
#             bet = j-i
#             for k in range(1,n-i-j):
#                 # print(i,i+j,i+j+k)
#                 if(a!=s[i+j+k] and k!=j and s[i+j]!=s[i+j+k]):
#                     count+=1
# print(count)