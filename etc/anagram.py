s1 = input()
s2 = input()

cA = ord('a')

s1 = [ord(e) - cA for e in s1]
l1 = len(s1)
s2 = [ord(e) - cA for e in s2]
l2 = len(s2)

ans = 0
for l in range(1, min(l1, l2) + 1):
    s = set()
    use = [0] * 26

    for i in range(l - 1):
        use[s1[i]] += 1
    for i in range(l - 1, l1):
        use[s1[i]] += 1
        s.add(tuple(use))
        use[s1[i - l + 1]] -= 1

    cnt = [0] * 26
    for i in range(l - 1):
        cnt[s2[i]] += 1
    for i in range(l - 1, l2):
        cnt[s2[i]] += 1
        if tuple(cnt) in s:
            ans = l
            break
        cnt[s2[i - l + 1]] -= 1
print(ans)
