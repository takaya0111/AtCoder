x = int(input())
hap = 0
a = int(x/(500))
hap +=a*1000
x %= 500
a = int(x/(5))
hap +=a*5
print(hap)