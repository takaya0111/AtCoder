s = str(input())
m = s[::-1]
n = len(s)
c=0
for i in range(int((n-1)/2)):
    if (s[i]!=m[i]):
        print("No")
        c=1
        break

if c==0:
    a = s[:int((n-1)/2)]
    b = s[int((n+1)/2):]
    x = a[::-1]
    y = b[::-1]
    # print(a)
    # print(b)

    l = (n+1)/4
        # print(l)

    for i in range(int(l)):
        if (a[i]!=x[i])or (b[i]!=y[i]):
            print("No")
            c =1
            break
    if(c==0): 
        print("Yes")
        