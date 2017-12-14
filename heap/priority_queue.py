from heapq import heappush, heappop
pq = []
for s in iter(input, 'end'):
    if s[0] == "i":
        k = int(s.split()[1])
        heappush(pq, -k)
    else:
        print(-heappop(pq))
