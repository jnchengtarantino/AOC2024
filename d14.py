import numpy as np
from collections import Counter, defaultdict
from functools import reduce, cache
from itertools import accumulate, groupby
from math import lcm, prod
import re

def part1(lines, t):
    lims = (11, 7) if t else (101, 103)
    buckets = {
        (range(lims[0] // 2), range(lims[1] // 2)) : [],
        (range((lims[0] // 2) + 1, lims[0]), range(lims[1] // 2)) : [],
        (range(lims[0] // 2), range((lims[1] // 2) + 1, lims[1])) : [],
        (range((lims[0] // 2) + 1, lims[0]), range((lims[1] // 2) + 1, lims[1])) : []
    }

    bots = parseInput(lines)
    positions = [((x + 100 * vx) % lims[0], (y + 100 * vy) % lims[1]) for (x, y, vx, vy) in bots]
    for p in positions:
        for k in buckets.keys():
            if p[0] in k[0] and p[1] in k[1]: buckets[k].append(p)
    
    return prod([len(v) for v in buckets.values()])

def part2(lines):
    lims = (101, 103)
    bots = parseInput(lines)
    ps = [[x,y] for x, y, _, _ in bots]
    vs = [(vx, vy) for _, _, vx, vy in bots]

    for i in range(1, 101 * 103):
        for j in range(len(ps)):
            ps[j][0] = (ps[j][0] + vs[j][0]) % lims[0]
            ps[j][1] = (ps[j][1] + vs[j][1]) % lims[1]

        arr = [[ '.' for x in range(lims[0])] for y in range(lims[1])]
        for x, y in ps:
            arr[y][x] = 'X'
        
        print()
        print(i)
        for row in arr:
            print(''.join(row))

    
def parseInput(lines: list[str]):
    bots = []
    for line in lines:
        res = re.findall(r'-?\d+', line)
        bots.append(tuple(int(r) for r in res))
    return bots

if __name__ == "__main__":
    testFile = open("test.txt")
    testLines = testFile.readlines() 
    print(" --- TEST --- ")
    print(f'Part 1 : {part1(testLines, True)}')      
    testFile.close()

    inFile = open("in.txt") 
    inLines = inFile.readlines()
    print(" --- RESULT --- ")
    print(f'Part 1 : {part1(inLines, False)}')      
    print(f'Part 2 : {part2(inLines)}')
    inFile.close()