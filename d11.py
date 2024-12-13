import numpy as np
from collections import Counter, defaultdict
from functools import reduce, cache
from itertools import accumulate, groupby
from math import lcm
import re
from tqdm import tqdm

def part1(lines):
    d = parseInput(lines)
    return sum([evolve(x, 25) for x in d])

def part2(lines):
    d = parseInput(lines)
    return sum([evolve(x, 75) for x in d])

@cache
def evolve(x: int, remaining: int) -> int:
    if remaining == 0 : return 1
    elif x == 0: return evolve(1, remaining-1)
    elif len(str(x)) % 2 == 0: 
        s = str(x)
        return (evolve(int(s[:len(s)//2]), remaining - 1) + evolve(int(s[len(s)//2:]), remaining - 1))
    else: return evolve(x * 2024, remaining - 1)
    
def parseInput(lines: list[str]) -> list[int]:
    return [int(x) for x in lines[0].strip().split()]

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