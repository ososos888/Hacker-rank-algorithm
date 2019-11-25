#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries):
    #a = 배열 k = 로테이션 수
    
    for i in range(k):
        #맨 마지막 값을 배열 맨 앞에 추가
        a.insert(0,a[(len(a)-1)])
        #배열의 마지막 원소 삭제
        a.pop()
    d=[]
    #queries의 값을 할당한 배열을 새로 생성하여 return
    for i in range(len(queries)):
        d.append(a[queries[i]])
    
    return d

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()