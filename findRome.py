#!/bin/python3

import math
import os
import random
import re
import sys

# Finding ROME :)


#
# Complete the 'find_rome' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY roads
#

def find_rome(n, roads):

    if len(roads) == 0: return -1

    out_city_dict = {}
    in_city_dict = {}

    for city in range(1, n + 1):
        out_city_dict[city] = []
        in_city_dict[city] = []

    for road in roads:
        out_city_dict[road[0]].append(road[1])
        in_city_dict[road[1]].append(road[0])

    candidates_rome = []
    for city in range(1, n + 1):
        if len(out_city_dict[city]) == 0 and len(in_city_dict[city]) == n - 1:
            candidates_rome.append(city)

    if len(candidates_rome) != 1: return -1
    return candidates_rome[0]





