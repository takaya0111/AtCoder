# import math
s = (input()[::-1]) # 入力文字列を逆順でsに格納
n = len(s)
counts = [0]*2019
counts[0]=1
b = 1
num = 0
for i in s:
    num += int(i)*b
    num %=2019
    b *=10
    b %=2019
    counts[num]+=1

# print(counts)
ans = 0
for j in counts:
    ans +=j*(j-1)/2


print(int(ans))



# counts = [0] * 2019
# counts[0] = 1

# num, d = 0, 1

# for char in s:
#     num += int(char) * d
#     num %= 2019
#     d *= 10
#     # d %= 2019
#     counts[num] += 1

# ans = 0
# for cnt in counts:
#     ans += cnt * (cnt - 1) // 2

# print(ans) # 答えの出力