N, K = map(int, input().split())
A = input().split()
A = [int(a) for a in A]
S = [1]
a = 1
number = 0
numbers=[-1 for _ in range(N)]
for _ in range(N + 1):
    b = A[a - 1]
    if numbers[b-1] != -1:
      c=numbers[b-1]          #1回目にループが現れた回数-1
      print("ループの最初の数字",b,"最初は"+str(c+1)+"回目","周期は",number-c)
      break
    numbers[b-1]=number
    number += 1
    S.append(b)
    a = b
T = S[c+1:number+1]
if K <= number:
  print("ループなし")
  print(S[K ])
else:
  z = K - c-1
  y = z % (number - c)
  print(y)
  print(T[y])