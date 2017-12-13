import math
from sys import stdin
from collections import defaultdict

class exist_negative_cycle(Exception):
    pass

inf = float('inf')

# ベルマンフォード
# O(E + V)
def bellman_ford(g, size, start=0):
    d = [inf] * size
    d[start] = 0

    for _ in range(size):
        for u in g:
            for v, d in g[u]:
                if d[v] > d[u] + d:
                    d[v] = d[u] + d

    for u in g:
        for v, d in g[u]:
            if d[v] > d[u] + d:
                raise exist_negative_cycle
    return d

v, e, r = map(int, input().split())

g = defaultdict(list)
for i in range(e):
    s, t, d = map(int, readline().split())
    g[s].append((t, d))

try:
    d = bellman_ford(g, v, r)
    for di in d:
        print('INF' if math.isinf(di) else di)

except exist_negative_cycle:
    print('NEGATIVE CYCLE')
