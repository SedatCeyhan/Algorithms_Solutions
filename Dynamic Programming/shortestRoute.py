#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'shortestRoute' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING route as parameter.
#

def shortestRoute(route):
    # Write your code here

    if len(route) == 0: return 0

    # Get the unique chars in the route
    # The list of all unique chars in the route
    numUniqueChars = len(list(set(route)))

    # left and right pointer to mark the smallest substring
    left, right = 0, 0

    # When this number equals numUniqueChars, this means that our substring
    # is a valid candidate containing all of its unique chars (We're interested in the shortest such candidate)
    uniqueChars_so_far = 0

    # initialize a dictionary with unique char keys
    # with each unique char value = 0
    # increment the value of the chars as we encounter them in the substring
    substring_uniqChar_dict = {}
    for uniq_char in list(set(route)):
        substring_uniqChar_dict[uniq_char] = 0

    shortest = float("inf")
    while right < len(route):
        curr_char = route[right]

        substring_uniqChar_dict[curr_char] = substring_uniqChar_dict[curr_char] + 1

        # First time encountered, so we increment the value of total unique chars encountered so far.
        if substring_uniqChar_dict[curr_char] == 1:
            uniqueChars_so_far += 1

        # If we found a substring that is a valid candidate containing at least one of its unique chars,
        # Then increment the value of left index to find other valid candidates that are shorter than the previous
        # valid substring.
        # We leave the loop and continue increasing the RIGHT index when we loose a unique char discovered before,
        while left <= right and uniqueChars_so_far == numUniqueChars:
            curr_char = route[left]

            # Save the smallest window until now.
            if right - left + 1 < shortest:
                shortest = right - left + 1

            substring_uniqChar_dict[curr_char] -= 1
            if substring_uniqChar_dict[curr_char] == 0:
                uniqueChars_so_far -= 1

            left += 1

        # Increase the right index to find more unique chars
        right += 1

    return shortest





print(shortestRoute(""))

