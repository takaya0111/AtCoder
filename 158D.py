s = input()
q = int(input())
a = []
# for j in range(q):
#     a.extend([list(map(str,input().split()))])
# # print(a)
# for i in a:
pre = ""
nex = ""
c = 1
TFC = [input().split() for _ in range(q)]
for i in TFC:
# for j in range(q):
#     i = list(map(str,input().split()))
    if i ==["1"]:
        c *= -1
        # s = s[::-1]
    elif i[0]=="2" and i[1]=="1":
        # s = i[2]+s
        if c == 1:
            pre=pre+i[2]
        else:
            nex = nex + i[2]
    elif i[0]=="2" and i[1]=="2":
        # s = s +i[2]
        if c ==1:
            nex = nex +i[2]
        else:
            pre = pre+i[2]
if c==-1:
    print(nex[::-1]+s[::-1]+pre)
else:
    print(pre[::-1]+s+nex)
# s = pre+s+nex
# if c ==-1:
#     s = s[::-1]
# print(s)