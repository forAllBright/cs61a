#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ucb import trace


def is_LinkedList(L):
    if L == 'empty':
        return True
    else:
        return len(L) == 2 and is_LinkedList(L[1])


def link(first, rest):
    assert is_LinkedList(rest)
    return [first, rest]


def build_linklist_from_arr(arr):
    if len(arr) == 1:
        return link(arr[0], 'empty')
    else:
        return link(arr[0], build_linklist_from_arr(arr[1:]))


def getFirst(L):
    assert is_LinkedList(L)
    assert L != 'empty'
    return L[0]


def getRest(L):
    assert is_LinkedList(L)
    assert L != 'empty'
    return L[1]


def len_linked_chain(L):
    if L == 'empty':
        return 0
    else:
        return 1 + len_linked_chain(L[1])


demo_linkedlist = build_linklist_from_arr([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(demo_linkedlist)
print(getFirst(demo_linkedlist))
