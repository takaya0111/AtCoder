k =int(input())
a,b = map(int,input().split())
c = 0
for i in range(a,b+1):
    if i%k==0:
        print("OK")
        c=1
        break
if c==0:
    print("NG")

    