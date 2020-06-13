import sys
sys.setrecursionlimit(10**7)
h,w = map(int,input().split())
# c = [list(input()) for i in range(h)]
c=[input().split() for _ in range(h)]
print(c)

def dfs(x,y):
    if not(0<=x<h) or not(0<=y<w) or c[x][y]=="#":
        return
    if c[x][y]=="g":
        print("Yes")
        sys.exit()

    c[x][y]="#"
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    dfs(x+1,y)

for i in range(h):
    for j in range(w):
        if c[i][j]=="s":
            startx,starty=i,j
            break

dfs(startx,starty)
print("No")