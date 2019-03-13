# -*- coding: utf-8 -*-
# @Author: forAllBright
# @Date:   2018-12-03 21:46:18
# @Last Modified by:   forAllBright
# @Last Modified time: 2018-12-03 23:25:04

class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest.__getitem__(i - 1)

    def __len__(self):
        if self.rest == self.empty:
            return 1
        else:
            return 1 + self.rest.__len__()

    def link_express(self):
        if self.rest == self.empty:
            return "Link({})".format(self.first)
        else:
            return "Link({}, {})".format(self.first, self.rest.link_express())

    def extend_link(self, moreLink):
        if self.rest == Link.empty:
            return Link(self.first, moreLink)
        else:
            return Link(self.first, self.rest.extend_link(moreLink))

    def map_link(self,f):
        if self.rest == Link.empty:
            return Link(f(self.first))
        else:
            return Link(f(self.first), self.rest.map_link(f))

    def link_filter(self,f):
        if self.rest == Link.empty:
            return self if f(self.first) else empty()
        else:
            if f(self.first):
                return Link(self.first, self.rest.link_filter(f))
            else:
                return self.rest.link_filter(f)

    def link_joint(self):
        if self.rest == Link.empty:
            return '{}'.format(self.first)
        else:
            return '{}{}'.format((self.first),self.rest.link_joint())

lin = Link(1, Link(2, Link(3)))
print(lin.first)
print(lin.__getitem__(1))
print(len(lin))
print(lin.link_express())
print(Link(3, Link(4, Link(5))).extend_link(Link(3, Link(4, Link(5)))).link_express()
)
print(lin.map_link(lambda x: x * x).link_express())

print(lin.link_filter(lambda x: x > 1).link_express())

print(lin.link_joint())
