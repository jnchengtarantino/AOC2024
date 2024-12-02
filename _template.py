import numpy as np
from collections import Counter, defaultdict
from functools import reduce, cache
from itertools import accumulate, groupby
from math import lcm
import re

def part1(lines):
    pass

def part2(lines):
    pass
    
def parseInput(lines):
    pass

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