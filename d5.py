import numpy as np
from collections import Counter, defaultdict
from functools import reduce, cache
from itertools import accumulate, groupby
from math import lcm
import re

def part1(lines):
    rules, rows = parseInput(lines)

    sum = 0
    for row in rows:
        tests = []
        for i in range(len(row)):
            for j in range(i+1, len(row)):
                tests.append((row[i], row[j]))
        
        if not any([i in rules[j] for i, j in tests]):
            sum = sum + row[(len(row))//2]
        
    return sum

def part2(lines):
    rules, rows = parseInput(lines)
    sum = 0
    wronglyOrdered = []

    for row in rows:
        tests = []
        for i in range(len(row)):
            for j in range(i+1, len(row)):
                tests.append((row[i], row[j]))
        
        if any([i in rules[j] for i, j in tests]):
            wronglyOrdered.append(row)



    for row in wronglyOrdered:

        for i in range(len(row)):
            for j in range(i+1, len(row)):
                if row[i] in rules[row[j]]:
                    row[i], row[j] = row[j], row[i]

        sum = sum + row[(len(row))//2]
    
    return sum
    
def parseInput(lines):
    rules = defaultdict(list)
    rows = []

    for line in lines:
        if '|' in line:
            a, b = line.strip().split('|')
            rules[int(a)].append(int(b))
        
        if ',' in line:
            rows.append([int(x) for x in line.strip().split(',')])
    
    return rules, rows
            

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