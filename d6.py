import numpy as np
from collections import Counter, defaultdict
from functools import reduce, cache
from itertools import accumulate, groupby
from math import lcm
import re

dir = [(-1,0), (0,1), (1,0), (0,-1)]

def part1(lines):
    bounds = (len(lines), len(lines[0].strip()))
    obstacles, guard = parseInput(lines)
    _, visited = traverse(guard, obstacles, bounds)
    return len({(y,x) for y, x, d in visited})

def part2(lines):
    obstacles, guard = parseInput(lines)
    bounds = (len(lines), len(lines[0].strip()))
    _, visited = traverse(guard, obstacles, bounds)
    testCandidates = {(y,x) for y, x, d in visited}
    count = 0

    for testObstacle in testCandidates:
        isLoop, _ = traverse(guard, obstacles, bounds, testObstacle)
        if isLoop: count = count + 1
    
    return count


def traverse(guard, obstacles, bounds, testObstacle = None):
    visited = set()
    while (guard not in visited) and (0 <= guard[0] < bounds[0]) and (0 <= guard[1] < bounds[1]):
        visited.add(guard)
        d = dir[guard[2]]
        if (guard[0] + d[0], guard[1] + d[1]) in {*obstacles, testObstacle}:
            guard = (guard[0], guard[1], (guard[2] + 1) % 4 )
        else:
            guard = (guard[0] + d[0], guard[1] + d[1], guard[2])
    
    return guard in visited, visited
    

    
def parseInput(lines):
    obstacles = set()
    guard = ()
    for i, line in enumerate(lines):
        for j, c in enumerate(line.strip()):
            if c == '#' :
                obstacles.add((i,j))
            if c == '^':
                guard = (i,j,0)
    
    return obstacles, guard    

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