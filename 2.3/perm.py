# -*- coding: utf-8 -*-
# @Author: forAllBright
# @Date:   2018-11-18 20:39:22
# @Last Modified by:   forAllBright
# @Last Modified time: 2018-11-18 21:11:56

from ucb import trace


def perm(prefix,str):
    if len(str)==0:
        print(prefix)
        return 1
    else:
        coun = 0
        for i in str:
            new_prefix = prefix + i
            rest = str_pop(str,i)
            coun = coun + perm(new_prefix,rest)
        return coun

def str_pop(s,c):
    assert c in s
    i = s.index(c)
    return s[:i] + s[i+1:]

ct = perm("","abcd")
print(ct)
