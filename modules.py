

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

print(array)

from fractions import gcd
from copy import deepcopy
