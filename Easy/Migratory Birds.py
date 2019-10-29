#!/bin/python3

import math
import os
import random
import re
import sys
import collections

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    freq = collections.Counter(arr)
    return max(freq, key=freq.get)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
