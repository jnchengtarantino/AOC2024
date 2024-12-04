import numpy as np
from collections import Counter, defaultdict
from functools import reduce, cache
from itertools import accumulate, groupby
from math import lcm
import re

def part1(lines):
    input = parseInput(lines)
    count = 0
    for i, line in enumerate(input):
        for j, c in enumerate(line):
            if c == 'X':
                for yDiff in [-1, 0, 1]:
                    for xDiff in [-1, 0, 1]:
                        if 'XMAS' == c + getOrDefault(input, i + yDiff, j + xDiff) + getOrDefault(input, i + 2*yDiff, j + 2*xDiff) + getOrDefault(input, i + 3*yDiff, j + 3*xDiff):
                            count = count+1

    return count

def part2(lines):
    input = parseInput(lines)
    count = 0
    mas = {'M','A','S'}
    for i, line in enumerate(input):
        for j, c in enumerate(line):
            if c == 'A':
                d1 = {c, getOrDefault(input, i-1,j-1), getOrDefault(input, i+1, j+1)}
                d2 = {c, getOrDefault(input, i-1,j+1), getOrDefault(input, i+1, j-1)}
                if d1 == mas and d2 == mas:
                    count = count+1                
    return count
    
def parseInput(lines):
    return [[c for c in line.strip()] for line in lines]

def getOrDefault(lines, i, j):
    if i < 0 or i >= len(lines) or j < 0 or j >= len(lines[0]):
        return '.'
    else:
        return lines[i][j]

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