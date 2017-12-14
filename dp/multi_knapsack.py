N, W = map(int, input().split())
dp = [0] * (W + 1)

for _ in range(N):
    v, w = map(int, input().split())
    for j in range(w, W + 1):
        dp[j] = max(dp[j], dp[j - w] + v)

print(dp[W])
