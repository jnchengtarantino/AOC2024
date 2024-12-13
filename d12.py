import numpy as np
from collections import Counter, defaultdict
from functools import reduce, cache
from itertools import accumulate, groupby
from math import lcm
import re

def part1(lines):
    garden = parseInput(lines)
    visited = set()
    return sum( map(lambda res: res[0] * (res[0]*4 - res[1]), [findPlot(y, x, garden, visited) for y in range(len(garden)) for x in range(len(garden[y])) if (y,x) not in visited]) )

def part2(lines):
    garden = parseInput(lines)
    visited = set()
    return sum( map(lambda res: res[0] * res[1], [findPlotCorners(y, x, garden, visited) for y in range(len(garden)) for x in range(len(garden[y])) if (y,x) not in visited]) )
    
def findPlot(y:int, x:int, garden: list[list[str]], visited: set[tuple[int,int]]) -> tuple[int,int]:
    visited.add((y,x))
    area, adj = 1, 0
    for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if inMap(garden, y + dy, x + dx) and garden[y+dy][x+dx] == garden[y][x]:
            adj = adj + 1
            if (y+dy, x+dx) not in visited:
                dArea, dAdj = findPlot(y+dy, x+dx, garden, visited)
                area = area + dArea
                adj = adj + dAdj
    
    return area, adj

def findPlotCorners(y:int, x:int, garden: list[list[str]], visited: set[tuple[int,int]]) -> tuple[int,int]:
    visited.add((y,x))
    area = 1
    corners = countCorners(y, x, garden)
    for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if inMap(garden, y + dy, x + dx) and garden[y+dy][x+dx] == garden[y][x] and (y+dy, x+dx) not in visited:
                dArea, dCorners = findPlotCorners(y+dy, x+dx, garden, visited)
                area = area + dArea
                corners = corners + dCorners
    return area, corners

def inMap(map: list[list], y: int, x: int) -> bool:
    return 0 <= y < len(map) and 0 <= x <len(map[0])

def countCorners(y:int, x:int, garden: list[list[str]]) -> int:
    corners = 0
    for dy, dx in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        # If not along an ongoing edge (which also includes if the adjactent block is a interior corner)
        if not (isSamePlot(garden, y, x, dy, 0) ^ isSamePlot(garden, y, x, 0, dx)):
            # If not an interior corner or exterior corner
            if (not isSamePlot(garden, y, x, dy, 0) and not isSamePlot(garden, y, x, 0, dx)) or (isSamePlot(garden, y, x, dy, 0) and isSamePlot(garden, y, x, 0, dx) and not isSamePlot(garden, y, x, dy, dx)):
                corners = corners + 1
    return corners

def isSamePlot(garden: list[list], y: int, x: int, dy: int, dx: int) -> bool:
    return inMap(garden, y+dy, x+dx) and garden[y+dy][x+dx] == garden[y][x]

def parseInput(lines: list[str]):
    return [[c for c in line.strip()] for line in lines]

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