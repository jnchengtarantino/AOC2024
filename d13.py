import numpy as np
from collections import Counter, defaultdict
from functools import reduce, cache
from itertools import accumulate, groupby
from math import lcm
import re

class Scenario:
    def __init__(self, ax, ay, bx, by, px, py):
        self.ax = int(ax)
        self.ay = int(ay)
        self.bx = int(bx)
        self.by = int(by)
        self.px = int(px)
        self.py = int(py)       

    def __repr__(self):
        return f'ax={self.ax}:ay={self.ay}:bx={self.bx}:by={self.by}:px={self.px}:py={self.py}'
    
    def getM(self):
        return np.array([[self.ax, self.bx], [self.ay, self.by]])
    
    def getP(self):
        return np.array([self.px, self.py])
    
    def getP2(self):
        return np.array([self.px + 10000000000000, self.py + 10000000000000])
    
def getMinPresses(s: Scenario, p2: bool) -> int:
    M = s.getM()
    P = s.getP() if not p2 else s.getP2()

    if np.linalg.det(M) != 0:
        X = np.linalg.solve(M, P)
        return 3 * round(X[0]) + round(X[1]) if isInt(X[0]) and isInt(X[1]) else 0
    else:
        return min(3 * (s.px//s.ax), s.px//s.bx) if isInt(s.px/s.ax) and (s.px / s.ax) == (s.py / s.ay) else 0
    
def isInt(x):
    return abs(x - round(x)) <= 0.0001



def part1(lines):
    scens = parseInput(lines)
    return sum([getMinPresses(s, False) for s in scens])

def part2(lines):
    scens = parseInput(lines)
    return sum([getMinPresses(s, True) for s in scens])
    
def parseInput(lines: list[str]) -> list[Scenario]:
    scens = []
    r = r'X\+?=?(\d+), Y\+?=?(\d+)'
    ax, ay, bx, by, px, py = -1, -1, -1, -1, -1, -1

    for i, line in enumerate(lines):
        if i % 4 == 3:
            continue

        res = re.search(r, line).group(1,2)
        if i % 4 == 0:
            ax, ay = res
        elif i % 4 == 1:
            bx, by = res
        elif i % 4 == 2:
            px, py = res
            scens.append(Scenario(ax, ay, bx, by, px, py))
    
    return scens


if __name__ == "__main__":
    testFile = open("test.txt")
    testLines = testFile.readlines() 
    print(" --- TEST --- ")
    print(f'Part 1 : {part1(testLines)}')      
    print(f'Part 2 : {part2(testLines)}')
    testFile.close()

    inFile = open("in.txt") 
    inLines = inFile.readlines()
    print(" --- RESULT --- ")
    print(f'Part 1 : {part1(inLines)}')      
    print(f'Part 2 : {part2(inLines)}')
    inFile.close()