n,m = map(int,input().split())
a = list(map(int,input().split()))
su = sum(a)
count = 0
for i in a:
    if i>=su/(4*m):
        count +=1
if count >=m:
    print("Yes")
else:
    print("No")
