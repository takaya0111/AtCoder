t = list(input())

for i in range(len(t)):
    if t[i]=="?":
        t[i]="D"
count = 0
for i in range(len(t)-1):
    if t[i]=="P" and t[i+1]=="D":
        count +=1
    elif t[i]=="D":
        count +=1
print("".join(t))

