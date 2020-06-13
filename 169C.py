import math
from decimal import Decimal
a,b = map(str,input().split())
a = Decimal(a)
b =Decimal(b)
# print('{:.020f}'.format(b))
# print(b)
# b *=100
# b = int(b)
# print(math.floor(a*b/100))
# c = a%10000
# e = math.floor(a / 10000)

# print(int(e*b*10000+c*b))

# c = b-int(b)
# for 
# d = int(b)
# s = a*d+c*a
print(int(math.floor(a*b)))