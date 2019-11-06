#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    #We need to find Kaprekar number in p to q
    d = []
    while p <= q:
        if p == 1: 
            d.append(p) 
        a = p*p
        alen = str(a)
        if (len(alen)//2) >= 1:
            k = (len(alen) // 2)
            #split number
            sp1 = int(alen[:k])
            sp2 = int(alen[k:])
            #Compare
            if sp1 + sp2 == p:
                d.append(p)
        p += 1
    if not d:
        d.append('INVALID RANGE')
    return (d)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    p = int(input())

    q = int(input())

    result = kaprekarNumbers(p, q)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
