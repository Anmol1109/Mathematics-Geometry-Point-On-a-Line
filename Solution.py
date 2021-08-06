#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    a = [0]*n
    b = [0]*n

    for n_itr in range(n):
        xy = input().split()

        x = int(xy[0])

        y = int(xy[1])
        
        a[n_itr], b[n_itr] = x,y
    if min(a) == max(a) or min(b) == max(b):
        print('YES')
    else:
        print('NO')
