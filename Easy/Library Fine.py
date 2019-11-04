#!/bin/python3

import math
import os
import random
import re
import sys
#제때 반납하면 요금 0
#제때 반납 못했지만 같은 달이면 15x 연체 일수
#제때 반납 못했지만 같은 해 이면 500x 연체 달수
#해가 지나면 무적권 10000
# Complete the libraryFine function below.
def libraryFine(d1, m1, y1, d2, m2, y2):
    a = 0
    if (y1 < y2) or (m1 < m2 and y1 == y2) or (d1 <= d2 and m1 == m2 and y1 == y2):
        a = 0
    elif (d1 > d2) and (m1 == m2) and (y1 == y2):
        a = (d1 - d2) * 15
    elif (m1 > m2) and (y1 == y2):
        a = (m1 - m2) * 500
    else:
        a = 10000
    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    d1M1Y1 = input().split()

    d1 = int(d1M1Y1[0])

    m1 = int(d1M1Y1[1])

    y1 = int(d1M1Y1[2])

    d2M2Y2 = input().split()

    d2 = int(d2M2Y2[0])

    m2 = int(d2M2Y2[1])

    y2 = int(d2M2Y2[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    fptr.write(str(result) + '\n')

    fptr.close()