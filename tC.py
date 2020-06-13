import sys
import numpy as np
n,k=map(int,input().split())
a =list(map(int,input().split()))
a = np.array(a)
c=0
if k>=n:
    print(*([n]*n))
    c = 1
if c==0:
    for _ in range(k):
        b = np.zeros(n)
        a = a.astype(np.int64)
        # print(b)
        # print(a.dtype)
        if not np.all(a==[n]*n):
            for i,j in enumerate(a):
                if j!=0:
                    x=max(i-j,0)
                    y=min(i+j+1,n)
                    b[x:y]+=1
                elif j==0:
                    b[i]+=1
                # print(b)
            a = b
    b = b.astype(np.int64)
    print(*b)