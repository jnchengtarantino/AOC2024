import numpy as np
from collections import Counter, defaultdict
from functools import reduce, cache
from itertools import accumulate, groupby
from math import lcm
import re

patt = r"mul\((\d{1,3}),(\d{1,3})\)"
patt2 = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"

def part1(lines):
    return sum([int(x)*int(y) for (x,y) in re.findall(patt, parseInput(lines))])

def part2(lines):
    dat = re.findall(patt2, parseInput(lines))
    do = True
    res = 0
    for d in dat:
        if d == "do()": do = True
        elif d == "don't()" : do = False
        elif do:
            m = re.match(patt, d)
            res = res + (int(m.group(1)) * int(m.group(2)))
    return res
    
def parseInput(lines):
    return ''.join([line for line in lines])

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