# -*- coding: utf-8 -*-
# @Author: forAllBright
# @Date:   2018-11-30 15:25:25
# @Last Modified by:   forAllBright
# @Last Modified time: 2018-12-03 20:58:24

#tree constructor, the formal is tree(label, tree(...), tree(...))


def tree(label,leftside=[],rightside=[]):
    '''
    tr = tree(1,tree(2,tree(3),tree(4)),tree(5,tree(tree(6),tree(7))))
    [[1, [2, [3], [4]], [5, [[[6]], [7]]]]]
    '''
    return [[label] + list(leftside) + list(rightside)]

def isTree(tree):
    if len(tree) == 0 or len(tree) > 2:
        return False
    else:
        for bran in getBranchesOfTree(tree):
            if not isTree(bran):
                return False
    return True

def isLeafOfTree(tree):
    return True if (len(tree) > 0 and getBranchesOfTree(tree) == []) else False

def getBranchesOfTree(tree):
    return tree[1:]

def maxDepthOfTree(tree):
    if isLeafOfTree(tree):
        return 1
    else:
        temp = []
        for bran in getBranchesOfTree(tree):
            temp.append(maxDepthOfTree(bran))
        return max(temp) + 1



# tr = tree(1,tree(2,tree(3),tree(4)),tree(5,tree(tree(6),tree(7))))
tr = tree(1,tree(2),tree(3,tree(4)))[0]
ttr = tree(2)
print(tr)
# print(isTree(tr))
# print(isLeafOfTree(tr))
# print(ttr)
print(getBranchesOfTree(tr))
print(isLeafOfTree(ttr))
print(isLeafOfTree(tr))
print(maxDepthOfTree(tr))

