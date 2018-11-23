# -*- coding: utf-8 -*-
# @Author: forAllBright
# @Date:   2018-11-21 14:13:58
# @Last Modified by:   forAllBright
# @Last Modified time: 2018-11-21 14:22:15

from functools import wraps

class Account():
    interest = 0.04

    def __init__(self, name):
        self.name = name
        self.interest = Account.interest

    def getName(self):
        return self.name


kit = Account("Kit")
Jin = Account("Jin")
print(kit.interest)
print(Jin.interest)

kit.interest = 0.08

print(kit.interest)
print(Jin.interest)
print(Account.interest)
