# https://www.hackerrank.com/challenges/ctci-linked-list-cycle
# https://en.wikipedia.org/wiki/Cycle_detection#Brent.27s_algorithm
# http://www.siafoo.net/algorithm/11


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def has_cycle(node):
    if node.next is None:
        return 0
    turtle, rabbit = node.data, node.data

    steps_taken, step_limit = 0, 2

    while True:
        # if rabbit == len(all_nodes) - 1:
        #    return 0

        rabbit = node.next
        steps_taken += 1

        if rabbit == turtle:
            return 1

        if steps_taken == step_limit:
            steps_taken = 0
            step_limit *= 2
            # teleport the turtle
            turtle = rabbit
