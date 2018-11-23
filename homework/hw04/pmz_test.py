# -*- coding: utf-8 -*-
# @Author: pmz
# @Date:   2018-11-23 12:00:32
# @Last Modified by:   pmz
# @Last Modified time: 2018-11-23 12:01:19

from hw04 import *

move_stack(9, 1, 3)
t, u, v = examples()
print(total_weight(t))

print(balanced(t))
print(balanced(u))
w = mobile(side(3, t), side(2, u))
print(balanced(w))
print(balanced(v))