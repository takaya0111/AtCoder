n,k = map(int,input().split())
s = list(map(int,input().split()))
# print(s)
now_city = 1
s_l_city = 1
t = [0] #何回そこを通ったか
f = [0] #何回目にそこを通ったか
a=0
b = 0#サイクルありなし
f_l=0#ループの最初
for i in range(n):
    t.append(0)
    f.append(-1)
# print(s)
sycle = 0
for i in range(1,n+10):
    now_city = s[now_city-1]
    
    if t[now_city-1]==1:
        #  print(i,f[j])
         sycle=i-f[now_city-1]
         f_l=f[now_city-1]
        #  f_l=i
        #  a = 1
         b = i
        #  s_l_city=now_city
        #  print("ループの最初の数字",now_city,"最初は"+str(f_l)+"回目","周期は",sycle)
         break
    t[now_city-1]+=1
    f[now_city-1]=i
# print(t)
# print(f_l)
# print(f_l,sycle,s_l_city)

if k>b:
    # now_city=s_l_city
    for _ in range((k-f_l)%sycle):
        
        now_city = s[now_city-1]
    # print((k-f_l)%sycle)
    print(now_city)
else:
    # print("ループなし")
    now_city=1
    for _ in range(k):
        now_city=s[now_city-1]
    print(now_city)

