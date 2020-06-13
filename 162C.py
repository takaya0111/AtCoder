import itertools
import math

k = int(input())
b = []
for i in range(1,k+1):
    b.append(i)
a = list(itertools.combinations_with_replacement(b, 3))
c = 0
for i in a:
    if (i[0]==i[1] or i[1]==i[2]):
        if (i[0]==i[1] and i[1]==i[2]):
         c += math.gcd(math.gcd(i[0],i[1]),i[2])
        else:
            c += 3* math.gcd(math.gcd(i[0],i[1]),i[2])
    else:
        c += 6*math.gcd(math.gcd(i[0],i[1]),i[2])

print(c)