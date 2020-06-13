#要素数カウントするやつ
import collections
l = ['a', 'a', 'a', 'b', 'c', 'c']
c = collections.Counter(l)
print(c)
# > Counter({'a': 3, 'c': 2, 'b': 1})

#長さが違う各行の入力をn回読み込む(1行を一つのリストに入れる)
ans = [input().split() for _ in range(n)]
#数値版
ans = [list(map(int,input().split())) for _ in range(n)]
#一文字ごとに区切ってリストに入れる(文字)
ans = [list(input()) for i in range(n)]

#空の2次元リスト定義
a = [[]for i in range(n)]

#listの末尾への追加はO(1)で行えるが、先頭への追加はO(N)かかる
#そこでdequeを使えば共にO(1)でできる！！
#dequeはリストを末尾にextendでそのまま追加できる
from collections import deque
d = deque()
d.extend([3,4]) 
d.append("a")                        #dequeにaddはない！
d.appendleft("b")
#リバースはlistの方が早いのでlistに戻してから行う
a = "".join(list(d))   #文字列の場合
a = a[::-1]

#Union Find Treeクラス
#出てくる数字が1~nのときはUnionFind(n+1)で初期化することで数字をそのまま使える
class UnionFind():
    def __init__(self,n):
        self.n = n
        self.parents = [-1]*n

    def find(self,x):
        if self.parents[x]<0:
            return x
        else:
            self.parents[x]=self.find(self.parents[x])
            return self.parents[x]
    
    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x==y:
            return
        if self.parents[x]>self.parents[y]:
            x,y=y,x
        self.parents[x]+=self.parents[y]
        self.parents[y]=x
    #木の深さじゃなくxを含む集合の要素数
    def size(self,x):
        return -self.parents[self.find(x)]

    def same(self,x,y):
        return self.find(x)==self.find(y)

    def members(self,x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i)==root]

    def roots(self):
        return [i for i,x in enumerate(self.parents) if x>0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())
