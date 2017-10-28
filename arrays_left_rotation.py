"""
https://www.hackerrank.com/challenges/ctci-array-left-rotation/
"""

from array import array
from itertools import chain, islice, tee


def get_numbers(intput_str):
    """yields only numbers from str"""
    numbers = array('u')
    to_int = lambda lst: int(''.join(lst))

    for i in intput_str:
        if i.isdigit():
            numbers.append(i)
        elif i == ' ' and numbers:
            yield to_int(numbers)
            numbers = []
        else:
            continue
    yield to_int(numbers)


number_of_digits, number_of_rotations = islice(
                                            get_numbers(intput_str=input()), 2)

assert number_of_digits and number_of_rotations

it = islice(get_numbers(intput_str=input()), number_of_digits)

head, tail = tee(it)

print(*(chain(islice(tail, number_of_rotations, None),
              islice(head, number_of_rotations))))
