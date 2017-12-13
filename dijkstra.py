from heapq import heappush, heappop
from pprint import pprint

inf = 1 << 30

# ダイクストラ with heap
# O((E + V)log V)
def dijkstra(n, edges, s):
    d = [inf] * n
    d[s] = 0
    pq = [(0, s)]
    fixed = 0
    while pq:
        di, v = heappop(pq)
        if di > d[v]:
            continue
        for u, c in edges[v]:
            if d[v] + c < d[u]:
                d[u] = d[v] + c
                heappush(pq, (d[u], u))
        fixed += 1
        if fixed == n - 1:
            break
    return d

n, m, s = map(int, input().split())

edges = [[] for i in range(n)]
for i in range(m):
    ui, vi, ci = map(int, input().split())
    edges[ui].append((vi, ci))

d = dijkstra(n, edges, s)
res = "\n".join(map(lambda v: str(v) if v < inf else "INF", d))
print(res)
