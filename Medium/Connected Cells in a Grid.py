#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the connectedCell function below.

def connected(matrix, i, j):
    if not (0 <= i < len(matrix)) or not (0 <= j < len(matrix[0])): # 주소가 -이면 0
        return 0
    if matrix[i][j] == 0: #cell값이 0이면 0
        return 0
    score = 1 #score 1 증가 후
    matrix[i][j] = 0 # cell 값을 0으로 바꾼다.
    for ii in range(i-1, i+2): # 중심을 기준으로 1인 cell을 search
        for jj in range(j-1, j+2):
            if i != ii or j != jj: # 중심 기준 대각선 값은 제외
                score += connected(matrix, ii, jj) #해당 cell의 값을 다시 search 
    return score

def connectedCell(matrix):
    score = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            score = max(score, connected(matrix, i, j))
    return score

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix)

    fptr.write(str(result) + '\n')

    fptr.close()