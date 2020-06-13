x = int(input())
a = 0
for i in range(-118,120):
    for j in range(-119,119):
        if(i**5-j**5==x):
            print(i,j)
            a=1
            break
    if a==1:
        break
