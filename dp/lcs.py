def memoize(f):
    cache = {}
    def helper(x, y):
        if x not in cache:
            cache[(x, y)] = f(x, y)
        return cache[(x, y)]
    return helper

# 最長共通部分列
@memoize
def lcs(a, b):
    if len(a) == 0 or len(b) == 0:
        return 0
    t = max(lcs(a, b[:-1]), lcs(a[:-1], b))
    if a[-1] == b[-1]:
        return max(lcs(a[:-1], b[:-1]) + 1, t)
    else:
        return t

n = int(input())
d = [(input(), input()) for _ in range(n)]

for (a, b) in d:
    print(lcs(a, b))
