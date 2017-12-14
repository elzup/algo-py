N, W = map(int, input().split())
dp = [[0] * (W + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    v, w = map(int, input().split())
    for j in range(w, W + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)

print(dp[N][W])
