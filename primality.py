"""
https://www.hackerrank.com/challenges/ctci-big-o
"""

from random import randint


# test ferma
def is_prime(n, tests_count):
    for i in range(tests_count):
        m = n - 1
        if (randint(1, m) ** m % n) != 1:
            return "Not prime"
    return "Prime"


p = int(input().strip())
for a0 in range(p):
    print(is_prime(int(input().strip()), 10))
