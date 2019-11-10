#!/bin/python3

import math
import os
import random
import re
import sys
import copy

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    #k = 사람수 c = 꽃 가격 list
    sum = 0
    count = 0
    d = copy.deepcopy(c)
    num = 0
    num = len(c)//k
    c.sort(reverse=True)
    d.sort(reverse=True)
    for z in range(num+1): 
        if count < num:
            for j in range(num):
                for i in range(k):
                    sum += c[0]
                    del c[0]
                    del d[0]
                count += 1
                #꽃다발 가격 증가
                for g in range(len(c)):
                    c[g] += d[g]

    #나머지 계산
    for i in range(len(c)):
        sum += c[i]
    return sum
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()