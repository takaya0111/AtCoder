n,k=map(int,input().split())
n_= n%k
l = n_-k
# print(n_,l)
if(n_>abs(l)):
    print(-l)
else:
    print(n_)