import numpy as np
from collections import Counter, defaultdict
from functools import reduce, cache
from itertools import accumulate, groupby
from math import lcm
import re

def part1(lines):
    l1, l2 = parseInput(lines)
    l1.sort()
    l2.sort()
    return sum([abs(n1-n2) for (n1,n2) in zip(l1,l2)])

def part2(lines):
    l1, l2 = parseInput(lines)
    count = Counter(l2)

    return sum([n * count.get(n, 0) for n in l1])
    
def parseInput(lines):
    l1, l2 = [], []
    for line in lines:
        (n1, n2) = line.split()
        l1.append(int(n1))
        l2.append(int(n2))

    return(l1, l2)


if __name__ == "__main__":
    testFile = open("test.txt")
    testLines = testFile.readlines() 
    print(" --- TEST --- ")
    print(part1(testLines))      
    print(part2(testLines))

    inFile = open("in.txt") 
    inLines = inFile.readlines()
    print(" --- RESULT --- ")
    print(part1(inLines))      
    print(part2(inLines))

    testFile.close()
    inFile.close()