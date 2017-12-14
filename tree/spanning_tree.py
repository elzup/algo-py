from operator import itemgetter

class UnionFind:
    def __init__(self, n):
        self.p = list(range(n))
        self.rank = [0] * n

    def find_root(self, x):
        if x != self.p[x]:
            self.p[x] = self.find_root(self.p[x])
        return self.p[x]

    def same(self, x, y):
        return self.find_root(x) == self.find_root(y)

    def unite(self, x, y):
        u = self.find_root(x)
        v = self.find_root(y)

        if u == v: return

        if self.rank[u] < self.rank[v]:
            self.p[u] = v
        else:
            self.p[v] = u

            if self.rank[u] == self.rank[v]:
                self.rank[u] += 1

# 最小全域木
# Cost昇順でまだ繋いでいない Node とつなぐ
# UnionFindTree
#
def main():
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    edges.sort(key=itemgetter(2), reverse=True)

    uf = UnionFind(n)

    ans = 0
    print(edges)

    for i in range(n - 1):
        while edges:
            s, t, w = edges.pop()

            if not uf.same(s, t):
                uf.unite(s, t)
                break

        ans += w

    print(ans)

if __name__ == '__main__':
    main()
