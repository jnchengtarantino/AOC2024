import numpy as np
from collections import Counter, defaultdict
from functools import reduce, cache
from itertools import accumulate, groupby
from math import lcm
import re

def part1(lines):
    dat = parseInput(lines)
    l, r = 0, len(dat) - 1
    while l < r:
        if dat[l][0] is None or dat[l][1] == 0:
            while not dat[r][0] or not dat[r][1]: r = r - 1
            if dat[l][1] <= dat[r][1]:
                dat[l] = (dat[r][0], dat[l][1])
                dat[r] = (dat[r][0], dat[r][1] - dat[l][1])
            else:
                dat.insert(l+1, (None, dat[l][1] - dat[r][1]))
                r = r + 1
                dat[l] = (dat[r][0], dat[r][1])
                dat[r] = (dat[r][0], 0)
        l = l + 1 
    
    datClean = [[x] * amount for x, amount in dat if x is not None and amount]
    flat = [inner for outer in datClean for inner in outer]
    return sum([i * c for i,c in enumerate(flat)])

def part2(lines):
    dat = parseInput(lines)
    for r in range(len(dat) - 1, -1, -1):
    
        if dat[r][0] is None or dat[r][1] == 0: continue
        for l in range(r):
            rx, rsize = dat[r]
            lx, lsize = dat[l]
            if lx is None and lsize >= rsize:
                dat[l] = (None, lsize-rsize)
                dat[r] = (None, rsize)
                dat.insert(l, (rx, rsize))
                break
    
    datClean = [[x] * amount for x, amount in dat if amount]
    flat = [inner for outer in datClean for inner in outer]
    return sum([i * c if c else 0 for i,c in enumerate(flat)])
    
def parseInput(lines: list[str]):
    ids = 0
    ret = []
    for i,c in enumerate(lines[0].strip()):
        if i % 2:
            ret.append((None, int(c)))
        else:
            ret.append((ids, int(c)))
            ids = ids + 1
    return ret

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