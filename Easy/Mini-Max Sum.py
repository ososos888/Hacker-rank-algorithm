#!/bin/python3

import math
import os
import random
import re
import sys
import copy

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arrmax = copy.deepcopy(arr)
    arrmin = copy.deepcopy(arr)
    arrmax.remove(max(arrmax))
    arrmin.remove(min(arrmin))

    return print(sum(arrmax, 0), sum(arrmin, 0))



if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
