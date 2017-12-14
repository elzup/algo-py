n = int(input())

edges = [None]
for i in range(n):
    edges.append(list(map(int, input().split()[2:])))

sndf = [None]
for i in range(1, n + 1):
    sndf.append([False, i])

path = []

time = 0

def dfs(u):
    global time
    sndf[u][0] = True
    time += 1
    sndf[u].append(time)

    for v in edges[u]:
        if not sndf[v][0]:
            dfs(v)
    time += 1
    sndf[u].append(time)


for i in range(1, n + 1):
    if not sndf[i][0]:
        dfs(i)

for x in sndf[1:]:
    print(*x[1:])
