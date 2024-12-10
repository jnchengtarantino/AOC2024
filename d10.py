import numpy as np
from collections import Counter, defaultdict
from functools import reduce, cache
from itertools import accumulate, groupby
from math import lcm
import re

def part1(lines):
    map = parseInput(lines)
    return sum([len(findTrailScore(y, x, map)) for y in range(len(map)) for x in range(len(map[y])) if map[y][x] == 0])

def findTrailScore(y:int, x: int, map: list[list[int]]) -> set[tuple[int,int]]:
    if map[y][x] == 9: return {(y,x)}
    return set().union(*[findTrailScore(y+dy, x+dx, map) for dy,dx in [(-1,0), (1,0), (0,-1), (0,1)] if inMap(map, y+dy, x+dx) and map[y][x] == map[y+dy][x+dx] - 1 ])



def part2(lines):
    map = parseInput(lines)
    return sum([findTrailRating(y, x, map) for y in range(len(map)) for x in range(len(map[y])) if map[y][x] == 0])

def findTrailRating(y: int, x: int, map: list[list[int]]) -> set[tuple[int,int]]:
    if map[y][x] == 9: return 1
    return sum([findTrailRating(y+dy, x+dx, map) for dy,dx in [(-1,0), (1,0), (0,-1), (0,1)] if inMap(map, y+dy, x+dx) and map[y][x] == map[y+dy][x+dx] - 1 ])
    


def parseInput(lines: list[str]):
    return [ [int(c) for c in line.strip()] for line in lines]

def inMap(map: list[list], y: int, x: int) -> bool:
    return 0 <= y < len(map) and 0 <= x <len(map[0])

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