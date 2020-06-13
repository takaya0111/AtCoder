a = [input().split() for _ in range(3)]
n = int(input())
b = [input() for _ in range(n)]

c = 0
for i in range(3):
    if a[0][i] in b and a[1][i] in b and a[2][i] in b:
        print("Yes")
        c = 1
        break
    if a[i][0] in b and a[i][1] in b and a[i][2] in b:
        print("Yes")
        c = 1
        break
if a[1][1] in b:
    if a[0][0] in b and a[2][2]in b and c==0:
        print("Yes")
        c = 1
    if a[0][2] in b and a[2][0]in b and c==0:
        print("Yes")
        c = 1 
if c == 0:
    print("No")