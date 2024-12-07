import numpy as np
from collections import Counter, defaultdict
from functools import reduce, cache
from itertools import accumulate, groupby
from math import lcm, log10
import re
from tqdm import tqdm

def part1(lines):
    count = 0
    input = parseInput(lines)
    for target, vals in input:
        target = int(target)
        vals = [int(v) for v in vals.strip().split(' ')]
        prev = [vals[0]]

        for i in range(1, len(vals)):
            curr = []
            for p in prev:
                curr = curr + addMul(p, vals[i])
            prev = curr

        if any([target == x for x in prev]):
            count = count + target
    
    return count

def part2(lines):
    count = 0
    input = parseInput(lines)
    for target, vals in tqdm(input):
        target = int(target)
        vals = [int(v) for v in vals.strip().split(' ')]
        prev = [vals[0]]

        for i in range(1, len(vals)):
            curr = []
            for p in prev:
                curr = curr + [x for x in addMulConcat(p, vals[i]) if x <= target]
            prev = curr

        if any([target == x for x in prev]):
            count = count + target
    
    return count

def addMul (a: int, b:int) -> list[int,int]:
    return [a+b, a*b]

def addMulConcat (a: int, b:int) -> list[int,int,int]:
    return [a+b, a*b, a * (10 ** (int(log10(b) + 1 ))) + b]
    
def parseInput(lines):
    return [line.strip().split(":") for line in lines]

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