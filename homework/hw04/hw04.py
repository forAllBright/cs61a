HW_SOURCE_FILE = 'hw04.py'

############
# Vitamins #
############


def make_counter():
    """Return a counter function.

    >>> c = make_counter()
    >>> c('a')
    1
    >>> c('a')
    2
    >>> c('b')
    1
    >>> c('a')
    3
    >>> c2 = make_counter()
    >>> c2('b')
    1
    >>> c2('b')
    2
    >>> c('b') + c2('b')
    5
    """
    db = {}

    def inner_counter(stuff):
        nonlocal db
        db[stuff] = db[stuff] + 1 if stuff in db else 1
        return db[stuff]
    return inner_counter


def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    """
    count = 0
    base0 = 0
    base1 = 1

    def inner_fib():
        nonlocal count, base0, base1
        if count == 0:
            count = count + 1
            return base0
        elif count == 1:
            count = count + 1
            return base1
        else:
            base1, base0 = base1 + base0, base1
            count = count + 1
            return base1
    return inner_fib

###################
# Towers of Hanoi #
###################


def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)


def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    pair = [start, end]
    mid = 0
    for i in range(4)[1:]:
        if i not in pair:
            mid = i
    if n == 1:
        print_move(start, end)
        return None
    else:
        move_stack(n - 1, start, mid)
        print_move(start, end)
        move_stack(n - 1, mid, end)
        return None

###########
# Mobiles #
###########


def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)


def label(tree):
    return tree[0]


def branches(tree):
    return tree[1:]


def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree):
    return not branches(tree)


def mobile(left, right):
    """Construct a mobile from a left side and a right side."""
    return tree(None, [left, right])


def sides(m):
    """Select the sides of a mobile."""
    return branches(m)


def side(length, mobile_or_weight):
    """Construct a side: a length of rod with a mobile or weight at the end."""
    return tree(length, [mobile_or_weight])


def length(s):
    """Select the length of a side."""
    return label(s)


def end(s):
    """Select the mobile or weight hanging at the end of a side."""
    return branches(s)[0]


def weight(size):
    """Construct a weight of some size."""
    assert size > 0
    return tree(size, [])


def size(w):
    """Select the size of a weight."""
    return label(w)


def is_weight(w):
    """Whether w is a weight, not a mobile."""
    return True if is_leaf(w) else False


def examples():
    t = mobile(side(1, weight(2)),
               side(2, weight(1)))
    u = mobile(side(5, weight(1)),
               side(1, mobile(side(2, weight(3)),
                              side(3, weight(2)))))
    v = mobile(side(4, t), side(2, u))
    return (t, u, v)


def total_weight(m):
    """Return the total weight of m, a weight or mobile.

    >>> t, u, v = examples()
    >>> total_weight(t)
    3
    >>> total_weight(u)
    6
    >>> total_weight(v)
    9
    """
    if is_weight(m):
        return size(m)
    else:
        return sum([total_weight(end(s)) for s in sides(m)])


def balanced(m):
    """Return whether m is balanced.

    >>> t, u, v = examples()
    >>> balanced(t)
    True
    >>> balanced(v)
    True
    >>> w = mobile(side(3, t), side(2, u))
    >>> balanced(w)
    False
    >>> balanced(mobile(side(1, v), side(1, w)))
    False
    >>> balanced(mobile(side(1, w), side(1, v)))
    False
    """
    if is_weight(m):
        return True
    pair = []
    for si in sides(m):
        pair.append(length(si) * total_weight(si[1]))
    assert len(pair) >= 1
    if pair[0] != pair[1]:
        return False
    else:
        for si in sides(m):
            if not balanced(si[1]):
                return False
        return True


def get_mobile_weight_from_side(s):
    return s[1]


def with_totals(m):
    """Return a mobile with total weights stored as the label of each mobile.

    >>> t, _, v = examples()
    >>> label(with_totals(t))
    3
    >>> print(label(t))                           # t should not change
    None
    >>> label(with_totals(v))
    9
    >>> [label(end(s)) for s in sides(with_totals(v))]
    [3, 6]
    >>> [label(end(s)) for s in sides(v)]         # v should not change
    [None, None]
    """
    if is_weight(m):
        return m
    else:
        new_sides = [side(length(si), with_totals(end(si))) for si in sides(m)]
        return tree(total_weight(m), new_sides)


#############
# Intervals #
#############


class interval:
    """A range of floating-point values.

    >>> a = interval(1, 4)
    >>> a
    interval(1, 4)
    >>> print(a)
    (1, 4)
    >>> a.low()
    1
    >>> a.high()
    4
    >>> a.width()
    3
    >>> b = interval(2, -2)  # Order doesn't matter
    >>> print(b, b.low(), b.high())
    (-2, 2) -2 2
    >>> a + b
    interval(-1, 6)
    >>> a - b
    interval(-1, 6)
    >>> a * b
    interval(-8, 8)
    >>> b / a
    interval(-2.0, 2.0)
    >>> a / b
    ValueError
    >>> -a
    interval(-4, -1)
    >>> c = interval(2, 8)
    >>> c + c
    interval(4, 16)
    >>> c - c
    interval(-6, 6)
    >>> c / c
    interval(0.25, 4.0)
    """

    # In all methods below, use the following method to create new intervals.
    # For example, if a method must return interval(x, y), have it
    # return self.makeinterval(x, y) instead.
    def make_interval(self, low, high):
        """Returns an interval of the same type as SELF with bounds LOW
        and HIGH.  Thus, if SELF is an interval, returns interval(LOW, HIGH)."""
        return interval(low, high)

    def __init__(self,low,high):
        self.lo = low
        self.hi = high

    def __repr__(self):
        return('interval({}, {})'.format(self.lo,self.hi))

    def __str__(self):
        return('({}, {})'.format(self.low(),self.high()))

    def low(self):
        return min(self.lo,self.hi)

    def high(self):
        return max(self.lo,self.hi)

    def width(self):
        if self.lo <= self.hi:
            return self.hi - self.lo
        else:
            return self.lo - self.hi

    def __add__(self,other):
        this = [self.lo,self.hi]
        that = [other.lo,other.hi]
        x = min(this) + min(that)
        y = max(this) + max(that)
        return self.make_interval(x,y)

    def __neg__(self):
        x, y = 0 - self.lo, 0 - self.hi
        return self.make_interval(min(x,y), max(x,y))

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self,other):
        p1 = self.lo * other.lo
        p2 = self.lo * other.hi
        p3 = self.hi * other.lo
        p4 = self.hi * other.hi
        return self.make_interval(min(p1,p2,p3,p4),max(p1,p2,p3,p4))

    def __truediv__(self,other):
        if other.lo + other.hi == 0:
            raise ValueError
        else:
            p1 = self.lo*1.0 / other.lo
            p2 = self.lo*1.0 / other.hi
            p3 = self.hi*1.0 / other.lo
            p4 = self.hi*1.0 / other.hi
            return self.make_interval(min(p1,p2,p3,p4),max(p1,p2,p3,p4))

class centered_interval(interval):

    def __init__(self, c, tol = None):
        """Initialize SELF to C +- TOL.  TOL is None, then C is assumed to be
        an interval, and SELF will be set to have the same bounds.
        >>> a = centered_interval(1, 2)
        >>> a.low()
        -1
        >>> a.high()
        3
        >>> a.width()
        4
        >>> b = centered_interval(3, 1)
        >>> a + b
        centered_interval(4.0, 3.0)
        >>> a * b
        centered_interval(4.0, 8.0)
        >>> -a
        centered_interval(-1.0, 2.0)
        """
        if tol is not None:
            super().__init__(c - tol, c + tol)
        else:
            super().__init__(c.lo, c.hi)

    def make_interval(self, low, high):
        """Returns a centered interval whose bounds are LOW and HIGH."""
        c = (low+high)*1.0/2
        tol = high - c
        return centered_interval(c, tol)

    def center(self):
        """The center of SELF.
        >>> centered_interval(5, 1).center()
        5.0
        >>> centered_interval(interval(4, 6)).center()
        5.0
        """
        return (self.lo + self.hi)*1.0/2

    def tolerance(self):
        """The tolerance of SELF.
        >>> centered_interval(5, 1).tolerance()
        1.0
        >>> centered_interval(interval(4, 6)).tolerance()
        1.0
        """
        return self.center() - self.lo

    def __str__(self):
        """A string representation of SELF as center +/- tolerance.
        >>> print(centered_interval(5, 1))
        5.0 +/- 1.0
        >>> print(centered_interval(interval(4, 6)))
        5.0 +/- 1.0
        """
        return "{} +/- {}".format(self.center(), self.tolerance())

    def __repr__(self):
        """A string represention of a Python expression that will produce SELF.
        >>> centered_interval(5, 1)
        centered_interval(5.0, 1.0)
        """
        return "centered_interval({}, {})".format(self.center(), self.tolerance())


###################
# Extra Questions #
###################

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    # return (lambda f: lambda k: f(f, k))(lambda f, k: k if k == 1 else mul(k, f(f, sub(k, 1))))
    # Alternate solution:
    #   return (lambda f: f(f))(lambda f: lambda x: 1 if x == 0 else x * f(f)(x - 1))
    return (lambda f: f(f))(lambda f: lambda x: 1 if x == 0 else x * f(f)(x - 1))


print(make_anonymous_factorial()(10))
