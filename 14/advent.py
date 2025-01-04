from collections import Counter, defaultdict, namedtuple, deque
from functools   import lru_cache, cmp_to_key, reduce, cache
from heapq       import heappop, heappush
from itertools   import permutations, combinations, chain, count as count_from, product as cross_product, groupby
from math        import ceil, inf, prod, remainder, gcd, floor
from statistics  import mean, median
from dataclasses import dataclass, field
from sys         import setrecursionlimit
import matplotlib.pyplot as plt
import networkx as nx
import re
import timeit
import unittest

def binary_search(predicate, low, high):
    """Return the minimum index, n, for which predicate(n) is
    True. Return None if not found"""
    found = False

    while high - low > 1:
        n = int((low + high) / 2)

        if predicate(n):
            found = True
            high = n
        else:
            low = n

    return high if found else None

def bool_list_to_decimal(lst):
    """Convert a list of boolean integers to the decimal equivalent."""
    return int("".join([ str(n) for n in lst ]), 2)

def compose(f, g):
    return lambda x: f(g(x))

def decimal_to_bool_list(n):
    return [ int(digit) for digit in bin(n)[2:] ]

def file_to_lines(fname):
    """Read a file and return a list of the lines in the file."""
    with open(fname) as myfile:
        return myfile.read().splitlines()

def findf(pred, seq):
    """Return the first element of a sequence satisfying the predicate,
       or None, if none is found."""
    return next((x for x in seq if pred(x)), None)

def grid_to_hash(lines,
                 elem_filter    = lambda x: True,
                 elem_transform = lambda x: x,
                 row_filter     = lambda x: True,
                 row_transform  = lambda x: x):
    return { complex(col, row) : elem_transform(elem)
             for row, line in enumerate(lines) if row_filter(line)
             for col, elem in enumerate(row_transform(line)) if elem_filter(elem) }

def grid_word_search(grid, word, dirs=(1, 1+1j, 1j, -1+1j, -1, -1-1j, -1j, 1-1j), offset=0):
    """Generate (x, y, direction) tuples for words in the grid. The
       dirs parameter specifies the allowable orientations, and the
       offset parameter allows shifting the word. Consider a 3-letter
       word. Using an offset of 0 would be typical and match words
       starting at (x, y). Using an offset of -1 would match words
       with the 2nd letter at (x, y)."""
    width     = len(grid[0])
    height    = len(grid)
    word_list = list(word)

    def get(c):
        x, y = int(c.real), int(c.imag)
        return grid[y][x] if 0 <= x < width and 0 <= y < height else None

    for dir in dirs:
        for x in range(width):
            for y in range(height):
                if word_list == [ get(complex(x,y) + (n + offset) * dir) for n in range(len(word)) ]:
                    yield (x, y, dir)

def iterate(fun, arg, n):
    """Return the result of repeatedly applying fun to arg n times."""
    for _ in range(n):
        arg = fun(arg)
    return arg

def partition(seq, pred):
    """Similar to filter, except a 2-tuple is returned: the items for which
       pred returns True, and the items for which pred returns False."""
    yes, no = [], []

    for item in seq:
        (yes if pred(item) else no).append(item)

    return yes, no

# Code from Peter Norvig's Advent of Code utilities

def atom(text):
    """Parse text into a single float or int or str."""
    try:
        x = float(text)
        return round(x) if round(x) == x else x
    except ValueError:
        return text

def atoms(text):
    """A tuple of all the atoms (numbers or symbol names) in text."""
    return mapt(atom, re.findall(r'[a-zA-Z_0-9.+-]+', text))

def digits(text):
    """A tuple of all the digits in text (as ints 0–9), ignoring non-digit characters."""
    return mapt(int, re.findall(r'[0-9]', text))

def ints(text):
    """A tuple of all the integers in text, ignoring non-number characters."""
    return mapt(int, re.findall(r'-?[0-9]+', text))

def mapt(fn, *args):
    """map(fn, *args) and return the result as a tuple."""
    return tuple(map(fn, *args))

def parse(day, parser=str, sep='\n', print_lines=None):
    """Split the day's input file into entries separated by `sep`, and apply `parser` to each."""
    fname    = f'day{day:02}.txt'
    the_file = open(fname, "r")
    text     = the_file.read()
    the_file.close()
    entries = mapt(parser, text.rstrip().split(sep))

    if print_lines:
        all_lines = text.splitlines()
        lines     = all_lines[:print_lines]
        head      = f'{fname} ➜ {len(text)} chars, {len(all_lines)} lines; first {len(lines)} lines:'
        dash      = "-" * 100

        print(f'{dash}\n{head}\n{dash}')

        for line in lines:
            print(trunc(line))

        print(f'{dash}\nparse({day}) ➜ {len(entries)} entries:\n'
              f'{dash}\n{trunc(str(entries))}\n{dash}')

    return entries

def quantify(iterable, pred=bool):
    """Count the number of items in iterable for which pred is true."""
    return sum(1 for item in iterable if pred(item))

def trunc(s: str, left=70, right=25, dots=' ... '):
    """All of string s if it fits; else left and right ends of s with dots in the middle."""
    dots = ' ... '
    return s if len(s) <= left + right + len(dots) else s[:left] + dots + s[-right:]

def words(text):
    """A list of all the alphabetic words in text, ignoring non-letters."""
    return re.findall(r'[a-zA-Z]+', text)