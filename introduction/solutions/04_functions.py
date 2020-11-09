#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# -----------------------------------------------------------------

from typing import List, Tuple

def word_counter(fname: str, nwds: int) -> List[Tuple]:
    """
    Return a list of tuple with the first words

    Parameters
    ----------
    fname : str
        Path to a text file.
    nwds : int
        Number of tuples to be returned.

    Returns
    -------
    words : List[tuple[str, int]]
        DESCRIPTION.

    """
    counter = {}
    with open(fname, 'r') as txt:
        for line in txt:
            for wd in line.lower().split():
                counter[wd] = 1 + counter.get(wd, 0)
    words = sorted(counter.keys())
    return [(wd, counter[wd]) for wd in words[:nwds]]

# -----------------------------------------------------------------

from typing import List, Tuple

def get_second(x):
    """Return the second element of a list"""
    return x[1]

def word_counter(fname: str, nwds: int) -> List[Tuple]:
    """
    Return a list of tuple with the first words

    Parameters
    ----------
    fname : str
        Path to a text file.
    nwds : int
        Number of tuples to be returned.

    Returns
    -------
    words : List[tuple[str, int]]
        DESCRIPTION.

    """
    counter = {}
    with open(fname, 'r') as txt:
        for line in txt:
            for wd in line.lower().split():
                counter[wd] = 1 + counter.get(wd, 0)
    words = sorted(counter.items(), key=get_second, reverse=True)
    return [(wd, counter[wd]) for wd in words[:nwds]]

# -----------------------------------------------------------------

from operator import itemgetter
    
# get_second = itemgetter(1)
def word_counter(fname: str, nwds: int) -> List[Tuple]:
    """
    Return a list of tuple with the first words

    Parameters
    ----------
    fname : str
        Path to a text file.
    nwds : int
        Number of tuples to be returned.

    Returns
    -------
    words : List[tuple[str, int]]
        DESCRIPTION.

    """
    counter = {}
    with open(fname, 'r') as txt:
        for wd in txt.read().lower().split():
            counter[wd] = 1 + counter.get(wd, 0)
    words = sorted(counter.items(), key=itemgetter(1), reverse=True)
    return words[:nwds]

word_counter("shakespeare.txt", 10)

# -----------------------------------------------------------------


def check(solution, attempt):
    """Return a tuple with the number of black and white. ::

    >>> check(['a', 'b', 'c', 'd', 'e'], ['e', 'd', 'c', 'b', 'a'])
    (1, 4)
    >>> check(['l', 'l', 'l', 'c'], ['c', 'c', 'c', 'c'])
    (1, 0)
    """
    solution1 = list(solution)
    white = 0
    for c in attempt:
        if c in solution1:
            white += 1
            solution1.remove(c)

    black = 0
    for a, s in zip(attempt, solution):
        if a == s:
            black += 1
    return black, white - black

# -----------------------------------------------------------------

def check2(solution, attempt):
    """Return a tuple with the number of black and white. ::

    >>> check2(['a', 'b', 'c', 'd', 'e'], ['e', 'd', 'c', 'b', 'a'])
    (1, 4)
    >>> check2(['l', 'l', 'l', 'c'], ['c', 'c', 'c', 'c'])
    (1, 0)
    """
    solution1 = list(solution)
    white = len([solution1.remove(c) for c in attempt if c in solution1])
    black = len([(a, s) for a, s in zip(attempt, solution) if a == s])
    return black, white - black

# -----------------------------------------------------------------

from random import choices


def check(solution, attempt):
    """Return a tuple with the number of black and white. ::

    >>> check2(['a', 'b', 'c', 'd', 'e'], ['e', 'd', 'c', 'b', 'a'])
    (1, 4)
    >>> check2(['l', 'l', 'l', 'c'], ['c', 'c', 'c', 'c'])
    (1, 0)
    """
    solution1 = list(solution)
    white = len([solution1.remove(c) for c in attempt if c in solution1])
    black = len([(a, s) for a, s in zip(attempt, solution) if a == s])
    return black, white - black

def user(length=4, validset=''):
    """Function that interface the user with the mastermind function."""
    return input("Try: ").split()

def mastermind(length=4, show=False, validset=None):
    validset = 'red green blue black yellow purple'.split() if validset is None else validset
    solution = choices(validset, k=length)
    print(f"Choose {length} colors from: {validset}")
    if show:
        print(f"[{' '.join(solution)}]")

    black = 0
    while black < length:
        attempt = user(length=length, validset=validset)
        if attempt == ["quit", ]:
            print(f"solution was: {solution}. Bye")
            return
        black, white = check(solution, attempt)
        print(" " * 15 + "BLACK: %d; WHITE: %d." % (black, white))
    print("Congratulations, you won!")
    
mastermind()


# -----------------------------------------------------------------

def percent(total, step, fill='#', empty='-', barsize=30):
    total -= 1

    def printpercent(i):
        rest = i / total
        ifill = int(rest * barsize)
        print(f"\r[{fill * ifill}{empty * (barsize - ifill)}] {int(rest * 100.):3d}%", end='', flush=True)
    return printpercent
