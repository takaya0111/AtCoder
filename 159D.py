n = int(input())
a = list(map(int,input().split()))
x = [0]*max(a)
for i in a:
    x[i-1]+=1
# print(x)
count = 0
# x_ = [(k*(k-1))/2 for k in x if k>=2]
# count = sum(x_)
for j in x:
    if j>=2:
        count += int((j*(j-1)/2))
for i in range(n):
    if x[a[i]-1]>=2:
        print(count-x[a[i]-1]+1)
    else:
        print(count)