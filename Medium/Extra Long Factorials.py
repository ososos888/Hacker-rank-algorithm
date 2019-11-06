#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    a = 1
    i = 1
    while i < n+1:
        a *= i
        i += 1
    print(a)

if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
