import math

# セグメント木

class segment_tree:
    def __init__(self, dat, q, default=0):
        self.offset = 2 ** math.ceil(math.log(len(dat), 2))
        self.table = [default] * self.offset + dat + [default] * (self.offset - len(dat))
        self.q = q
        for i in reversed(range(1, self.offset)):
            self.table[i] = self.q(self.table[2 * i], self.table[2 * i + 1])

    # [l, r] closed-interval
    def find(self, l, r):
        return self.q(self.__range(l,r))

    def __range(self, l, r):
        l += self.offset
        r += self.offset
        while l <= r:
            if l & 1:
                yield self.table[l]
                l += 1
            l >>= 1
            if r & 1 == 0:
                yield self.table[r]
                r -= 1
            r >>= 1

    def update(self, i, x):
        i += self.offset
        self.table[i] = x
        while 1 < i:
            i >>= 1
            self.table[i] = self.q(self.table[2 * i], self.table[2 * i + 1])

# Range Minimum Query (RMQ)

n, q = map(int, input().split())
rmq = segment_tree([(1 << 31) - 1] * n, min, float('inf'))

function = (rmq.update, lambda x, y:print(rmq.find(x, y)))
for com, x, y in (map(int, input().split()) for _ in range(q)):
    function[com](x, y)
