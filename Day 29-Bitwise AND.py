#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])
        max1 = 0
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                bit_and = i & j
                if k > bit_and > max1:
                    max1 = bit_and
        print(max1)
