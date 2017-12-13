import math
inf = float('inf')

# ワーシャルフロイド
# O(V^3)
def warshallFloyd(V, g):
    for k in range(V):
        for i in range(V):
            for j in range(V):
                g[i][j] = min(g[i][j], g[i][k] + g[k][j])

def main():
    V, E = map(int, input().split())
    g = [[inf] * V for _ in range(V)]
    for i in range(V):
        g[i][i] = 0
    for _ in range(E):
        f, t, d = map(int, input().split())
        g[f][t] = d
    # print(g)
    warshallFloyd(V, g)

    if any([g[i][i] < 0 for i in range(V)]):
        print('NEGATIVE CYCLE')
        return
    for d in g:
        to_s = lambda x: 'INF' if math.isinf(x) else str(x)
        print(' '.join(map(to_s, d)))

main()
