"""
https://www.hackerrank.com/challenges/ctci-fibonacci-numbers
"""

def fib(n):
    a, b = 0, 1
    while n:
        b, a, n = a, a + b, n - 1
    return a


print(fib(int(input())))
