a,b = map(int,input().split())
import math
c = 0
for i in range(10*b,10*b+10):
    if math.floor(i*0.08)>=a and math.floor(i*0.08)<a+1:
        print(i)
        c = 1
        break
if c == 0:
    print(-1)