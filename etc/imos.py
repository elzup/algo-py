
N, Q = map(int, input().split())
t = [0] * (N + 1)

for i in range(Q):
    l, r = map(int, input().split())
    t[l - 1] ^= 1
    t[r] ^= 1

k = 0
res = ""
for i in range(N):
    k ^= t[i]
    res += str(k)

print(res)
