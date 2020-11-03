#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import List, Iterable, Callable
from random import choices
from operator import itemgetter

def check(solution: List[str], attempt: List[str]) -> (int, int):
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


def user(board: List=None, length: int=4, validset: str=''):
    """Function that interface the user with the mastermind function."""
    return tuple(input("Try: "))


def solver(board: List=None, length: int=4, validset: str=''):
    """Function that use the previous attempts to identify the correct sequance"""
    exclude = set()
    if board is None:
        # guess 1st solution
        return choices(validset, k=length)
    elif len(board) == 1:
        # guess 2nd attempt
        for attempt, black, white in board:
            good = (black + white)
            if good == length:
                return choices(attempt, k=length)
            elif good > 0:
                newvals = (choices(attempt, k=good) + 
                           choices([x for x in validset if x not in attempt], 
                                   k=(length - good)))
                return choices(newvals, k=length)
            else:
                # everything to be excluded
                exclude.update(attempt)
                return choices([x for x in validset if x not in exclude], 
                                k=length)
    else:
        s_board = sorted(board, key=itemgetter(1, 2), reverse=True)
        print(s_board)
        return tuple("quit")

def mastermind(length: int = 4, 
               show: bool = False, 
               validset: Iterable[str] = 'abcdefghijkl',
               getattempt: Callable = user):
    """
    Play the Master mind game.

    Parameters
    ----------
    length : int, optional
        Length of the sequence to be found. The default is 4.
    show : bool, optional
        Show the solution together with the game's rule. The default is False.
    validset : Iterable[str], optional
        Define which are the valid possible user choices. The default is 'abcdefghijkl'.
    getattempt : Callable, optional
        Function used to get the next attempt. The default is user.

    Returns
    -------
    None.

    """
    solution = choices(validset, k=length)
    print(f"Choose {length} characters from: {validset}, type `quit` to exit from the game")
    if show:
        print(f"[the solution is: {''.join(solution)}]")

    board = []
    black = 0
    quit = False
    while black < length:
        attempt = getattempt(board=board, length=length, validset=validset)
        if attempt == tuple("quit"):
            print(f"The solution was: {''.join(solution)}\nbye")
            quit = True
            break
        black, white = check(solution, attempt)
        board.append((attempt, black, white))
        print(" " * 15 + "BLACK: %d; WHITE: %d." % (black, white))
    if not quit:
        print("Congratulations, you won!")
    
if __name__ == "__main__":
    mastermind(show=True)