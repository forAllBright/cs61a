#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ucb import trace


def tree(root_label, branches=[]):
    for branch in branches:
        assert is_tree(branch), "branch must be tree"
    return [root_label] + list(branches)


def label(tree):
    return tree[0]


def branches(tree):
    return tree[1:]


#  @trace


def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree):
    return not branches(tree)


def fib_tree(n):
    if n == 0 or n == 1:
        return tree(n)
    else:
        left, right = fib_tree(n - 2), fib_tree(n - 1)
        fib_n = label(left) + label(right)
        return tree(fib_n, [left, right])


def count_leaves(tree, sum=0):
    if is_leaf(tree):
        return 1
    else:
        for b in branches(tree):
            sum = sum + count_leaves(b)
        return sum


def partition_tree(n, m):
    if n == 0:
        return tree(True)
    elif m == 0 or n < 0:
        return tree(False)
    else:
        return tree(m, [partition_tree(n - m, m), partition_tree(n, m - 1)])


@trace
def print_parts(tree, partition=[]):
    if is_leaf(tree):
        if label(tree):
            print(' + '.join(partition))
    else:
        left, right = branches(tree)
        m = str(label(tree))
        print_parts(left, partition + [m])
        print_parts(right, partition)


if __name__ == "__main__":
    t = tree(1, [tree(2, [tree(4), tree(5)]), tree(3, [tree(7), tree(8)])])
    print(t)

    fib_T = fib_tree(9)
    print(fib_T)

    print(count_leaves(fib_tree(5)))

    partition_tree(2, 2)

    print_parts(partition_tree(6, 4))
