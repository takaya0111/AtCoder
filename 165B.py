x = int(input())
money=100
year = 0
while(True):
    year+=1
    money =int(money*1.01)
    if(money>=x):
        print(year)
        break
    