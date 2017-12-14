payment, _ = map(int, input().split())
coin = list(map(int, input().split()))
INF = float('inf')

dp = [INF] * (payment + 1)
dp[0] = 0

for ci in coin:
    for pi in range(ci, len(dp)):
        if dp[pi] > dp[pi - ci] + 1:
            dp[pi] = dp[pi - ci] + 1
print(dp[-1])
