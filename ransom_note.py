"""
https://www.hackerrank.com/challenges/ctci-ransom-note
"""

from collections import Counter, defaultdict

m, n = input().strip().split(' ')

words, ransom = input().strip(), input().strip()
w_d, r_d = defaultdict(int), defaultdict(int)

for w in words.split(' '):
    w_d[w] += 1

for r in ransom.split(' '):
    r_d[r] += 1

w_c, r_c = Counter(w_d), Counter(r_d)

w_c.subtract(r_c)
print("Yes" if not bool(-w_c) else "No")
