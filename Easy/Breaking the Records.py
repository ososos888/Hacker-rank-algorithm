#!/bin/python3

import math
import os
import random
import re
import sys
import copy

# Complete the breakingRecords function below.
def breakingRecords(scores):
    i = 1
    hs = copy.deepcopy(scores[0])
    hsa = 0
    ls = copy.deepcopy(scores[0])
    lsa = 0
    for i in range(len(scores)):
        if hs < scores[i]:
            hsa += 1 #count
            hs = copy.deepcopy(scores[i]) #input new max value
        elif ls > scores[i]:
            lsa += 1
            ls = copy.deepcopy(scores[i])
    return hsa, lsa
            


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()