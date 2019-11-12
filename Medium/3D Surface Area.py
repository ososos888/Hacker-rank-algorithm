#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the surfaceArea function below.
def surfaceArea(A):
    #6방향에서 본 cell의 넓이를 각가 구해 더한다.
    #위와 아래의 넓이
    fnc = 2*((H*W)-A.count(0))
    #앞뒤의 넓이
    frontsum = 0
    for j in range(W):
        for i in range(H):
            if i < H-1:
                frontsum += abs(A[i][j]-A[i+1][j])
            else:
                frontsum += A[i][j]
        frontsum += A[0][j]

    #양 side의 넓이
    sidesum = 0
    for i in range(H):
        for j in range(W):
            if j < W-1:
                sidesum += abs(A[i][j]-A[i][j+1])
            else:
                sidesum += A[i][j]
        sidesum += A[i][0]

    return (fnc+frontsum+sidesum)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
