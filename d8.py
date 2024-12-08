import numpy as np
from collections import Counter, defaultdict
from functools import reduce, cache
from itertools import accumulate, groupby
from math import lcm
import re

def part1(lines):
    antennae, xBound, yBound = parseInput(lines)
    antinodes = set()
    for k in antennae.keys():
        pairs = [(antennae[k][p1], antennae[k][p2]) for p1 in range(len(antennae[k])) for p2 in range(p1+1, len(antennae[k]))]
        antinodes |= {an for a,b in pairs for an in (2*a - b, 2*b - a) if an.real in range(xBound) and an.imag in range(yBound)}
    return len(antinodes)

def part2(lines):
    antennae, xBound, yBound = parseInput(lines)
    antinodes = set()
    for k in antennae.keys():
        pairs = [(antennae[k][p1], antennae[k][p2]) for p1 in range(len(antennae[k])) for p2 in range(p1+1, len(antennae[k]))]
        antinodes |= {a + n*(b-a) for a,b in pairs for n in range(-50,50) if (a + n*(b-a)).real in range(xBound) and (a + n*(b-a)).imag in range(yBound)}
    return len(antinodes)
    
def parseInput(lines):
    antennae = defaultdict(list)
    for y, line in enumerate(reversed(lines)):
        for x, c in enumerate(line.strip()):
            if c != '.' : antennae[c].append(x + (1j * y))
    return antennae, len(lines[0].strip()), len(lines)

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