"""
https://www.hackerrank.com/challenges/ctci-making-anagrams/
"""

from collections import Counter

c_a, c_b = Counter(input().strip()), Counter(input().strip())
print(sum((c_a - c_b).values()) + sum((c_b - c_a).values()))
