#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
#n 횟수 s 배열
    height = 0
    heightrecord = []
    valleycount = 0
    for i in range(len(s)):
        if s[i] == "U":
            height += 1
        else:
            height -= 1
        heightrecord.append(height)

    #-1->0으로 높이가 변하는 경우를 count
    j = 1
    for j in range(len(s)):    
        if heightrecord[j-1] == -1 and heightrecord[j] == 0:
            valleycount += 1
    return valleycount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()