# binary search
import bisect

array = [1, 3, 7, 9]
bisect.insort_left(array, 11)
bisect.insort_left(array, 5)



# sorted
print(array)
# [1, 3, 5, 7, 9, 11]

# search
bisect.bisect_left(array, 8)
# 4
bisect.bisect_left(array, 9)
# 4



# itemgetter
from operator import itemgetter

itemgetter(1, 3, 5)('ABCDEFG')
# ('B', 'D', 'F')

a = [["third", 3], ["first", 1], ["second", 2]]
a.sort(key=itemgetter(1))
a
# [['first', 1], ['second', 2], ['third', 3]]



# defaultdict
from collections import defaultdict
d = defaultdict(int)
for k in "toshino":
    d[k] += 1
d.items()
# [('t', 1), ('o', 2), ('s', 1), ('h', 1), ('i', 1), ('n', 1)]



# regex
m = r.search(r"[a-z]=\d$")
m.start()   # 4
m.end()     # 7
m.span()    # (4, 7)

r = re.compile("([a-z]+)=([0-9])"
m = r.search("abc=123&def=456")
m.group(1)      # 'abc'
m.group(1, 2)   # ('abc', '1')
m.groups()      # ('abc', '1')

m = r.findall("abc=123&def=456")
# [('abc', '1'), ('def', '4')]



# itertools
from itertools import permutations, combinations, product
permutations('ABCD', 2)     # AB AC AD BA BC BD CA CB CD DA DB DC
permutations(range(3))      # 012 021 102 120 201 210


combinations('ABCD', 2)     # AB AC AD BC BD CD
combinations(range(4), 3)   # 012 013 023 123

product('ABCD', 'xy')       # Ax Ay Bx By Cx Cy Dx Dy
product(range(2), repeat=3) # 000 001 010 011 100 101 110 111



# bit operators
hex(1023)
bin(15)
oct(7)

int("0x100", 16)
int("0b1111", 2)
int("0o1777", 8)

x | y   # or
x & y   # and
x ^ y   # xor
x << y  # left shift
x >> y  # right shift

bin((0b101110 >> 2) & 0b11)
'0b11'

bin(~1 & 0b1111)
'0b1110'

# other name note
from fractions import gcd
from copy import deepcopy
