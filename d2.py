import numpy as np
from collections import Counter, defaultdict
from functools import reduce, cache
from itertools import accumulate, groupby
from math import lcm
import re

def part1(lines):
    return sum([1 for line in parseInput(lines) if check(line)])

def part2(lines):
    return sum([1 for line in parseInput(lines) if checkDampened(line)])
    
def parseInput(lines):
    return [[int(x) for x in line.split()] for line in lines]

def check(line: list) -> bool:  
    if line[0] > line[1]:
        line.reverse()

    for i in range(1,len(line)):
        if not (1 <= line[i] - line[i-1] <= 3):
            return False
    
    return True

def checkDampened(line: list) -> bool:
    return check(line) or any([check(line[:x] + line[x+1:]) for x in range(len(line))])

if __name__ == "__main__":
    testFile = open("test.txt")
    testLines = testFile.readlines() 
    print(" --- TEST --- ")
    print(part1(testLines))      
    print(part2(testLines))
    testFile.close()

    inFile = open("in.txt") 
    inLines = inFile.readlines()
    print(" --- RESULT --- ")
    print(part1(inLines))      
    print(part2(inLines))
    inFile.close()