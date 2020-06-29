#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    binary=bin(n)
    binary=binary[2:]
    #print(binary)
    c=0
    mc=0
    for i in str(binary):
        if i=='1':
            c=c+1
        else:
            if c>mc:
                mc=c
            c=0
    if c>mc:
        mc=c
    print(mc)
