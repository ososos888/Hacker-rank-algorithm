#!/bin/python3

import math
import os
import random
import re
import sys

n=input()
l=list(map(int,input().split()))
d=[]
for x in l:
    diff=(len(l) -1 - l[::-1].index(x))-l.index(x)
    #diff = (배열l의 길이 - 1 - 배열l의 역순의 x라는 값이 있는 곳의 위치)-(l의 x가 있는 곳의 위치)
    if diff>0:
        d.append(diff) #배열 d에 diff의 값 추가
if len(d)==0:
    print('-1')
else:
    print(min(d))
