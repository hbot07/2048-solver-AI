import time

import sys

import math

from BaseAI import BaseAI

inf = float("inf")

sys.setrecursionlimit(10 ** 6)


def terminal_test(grid):
    return not grid.canMove()


def heuristic(grid):
    h_monotonicity = monotonicity(grid) / 8
    h_empty = len(grid.getAvailableCells()) / 16
    h_max_multiplier = math.log2(grid.getMaxTile())
    if grid.getMaxTile() == grid.map[0][0]:
        h_max_corner_multiplier = 2
    else:
        h_max_corner_multiplier = 1
    return h_monotonicity * h_empty * h_max_multiplier * h_max_corner_multiplier


def monotonicity(grid):
    n = grid.map
    m = list(map(list, zip(*n)))
    h = 0
    for i in range(len(n)):
        if all(earlier >= later for earlier, later in zip(n[i], n[i][1:])):
            h += 1
        if all(earlier >= later for earlier, later in zip(m[i], m[i][1:])):
            h += 1
    return h


def search_depth(grid):
    empty_cells = len(grid.getAvailableCells())
    if empty_cells >= 16:
        return 2
    elif empty_cells >= 8:
        return 4
    elif empty_cells >= 4:
        return 6
    else:
        return 8


class PlayerAI(BaseAI):

    def __init__(self):
        self.depth = 0
        self.max_search_depth = 0
        self.start_time = 0

    def getMove(self, grid):
        # moves = grid.getAvailableMoves()
        # return moves[randint(0, len(moves) - 1)] if moves else None
        self.start_time = time.clock()
        self.depth = 0
        self.max_search_depth = search_depth(grid)
        move, _, _ = self.maximize(grid, -inf, inf)
        return move

    def maximize(self, grid, alpha, beta):
        self.depth += 1
        if self.depth >= self.max_search_depth:
            return None, None, heuristic(grid)
        elif not grid.canMove():
            return None, None, heuristic(grid)
        elif time.clock() - self.start_time >= 0.099:
            return None, None, heuristic(grid)
        best_move, max_child, max_utility = None, None, -inf
        for move in sorted(map(int, grid.getAvailableMoves()), key=lambda num: num % 2):
            child = grid.clone()
            child.move(move)
            _, _, utility = self.minimize(child, alpha, beta)
            self.depth -= 1
            if utility > max_utility:
                best_move, max_child, max_utility = move, child, utility
            if max_utility >= beta:
                break
            if max_utility > alpha:
                alpha = max_utility
            if time.clock() - self.start_time >= 0.1:
                break

        return best_move, max_child, max_utility

    def minimize(self, grid, alpha, beta):
        self.depth += 1
        if self.depth >= self.max_search_depth:
            return None, None, heuristic(grid)
        elif not grid.canMove():
            return None, None, heuristic(grid)
        elif time.clock() - self.start_time >= 0.099:
            return None, None, heuristic(grid)
        best_move, min_child, min_utility = None, None, inf
        for cell in grid.getAvailableCells():
            gridCopy = grid.clone()
            gridCopy.setCellValue(cell, 2)
            _, _, utility = self.maximize(gridCopy, alpha, beta)
            self.depth -= 1
            if utility < min_utility:
                best_move, min_child, min_utility = cell, gridCopy, utility
            if min_utility <= alpha:
                break
            if min_utility < beta:
                beta = min_utility
            if time.clock() - self.start_time >= 0.1:
                break

        return best_move, min_child, min_utility
