n = int(input())
edges = [list(map(int, input().split()))[2:] for _ in range(n)]

d = [-1] * n

s = 1
q = []
d[s - 1] = 0
q.append(s)
while len(q):
    u = q.pop()
    v = edges[u - 1]
    for vi in v:
        if d[vi - 1] == -1:
            d[vi - 1] = d[u - 1] + 1
            q.append(vi)
        elif d[vi - 1] > d[u - 1] + 1:
            d[vi - 1] = d[u - 1] + 1
            q.append(vi)

for i, di in enumerate(d):
    print(i + 1, di)
