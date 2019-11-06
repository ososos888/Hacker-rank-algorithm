#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulTriplets function below.
def beautifulTriplets(d, arr):
    a = 0
    for i in range(len(arr)):
        #d 거리와 d2 거리만큼의 값이 배열에 존재하면 a는 1 증가
        if arr.count(arr[i]+d) != 0:
            if arr.count(arr[i]+(2*d)) != 0:
                a += 1
    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
