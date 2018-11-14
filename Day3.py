#!/bin/python3

import math
import os
import random
import re
import sys

def check(N):
    if N % 2 == 1:
        print ("Weird")
    elif N % 2 ==0:
        if 2 <= N <= 5:
            print ("Not Weird")
        elif 6 <= N <= 20:
            print ("Weird")
        elif 20 < N:
            print ("Not Weird")

if __name__ == '__main__':
    N = int(input())

    check(N)