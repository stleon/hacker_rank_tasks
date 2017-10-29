"""
https://www.hackerrank.com/challenges/ctci-bubble-sort
"""

# default part from task
n = int(input().strip())
lst = list(map(int, input().strip().split(' ')))


swaps = 0
is_sorted = False

def print_res(swaps, first, last):
    print("Array is sorted in %d swaps." % swaps)
    print("First Element: %d" % first)
    print("Last Element: %d" % last)

if len(lst) == 1:
    print_res(swaps=0, first=lst[0], last=lst[0])

while not is_sorted:
    is_sorted = True

    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            is_sorted = False
            swaps += 1
            lst[i], lst[i + 1] = lst[i + 1], lst[i]

print_res(swaps=swaps, first=lst[0], last=lst[-1])
