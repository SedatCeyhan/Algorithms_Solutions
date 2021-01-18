# Author: Kemal Sedat Ceyhan
# BlackRock Challenge 2
# I chose PYTHON for this challenge because I believe I'm really proficient in Python's String manipulation
# THANK YOU!

import sys

def doSomething(blobs, pattern):
    # Total number of matches to be appended at the end
    total = 0
    # Solution string consisting of matches separated by "|" with total number of matches as the last entry
    result = ""

    # CASE 1: empty pattern
    # If we have an empty pattern
    # Then every non-empty blob should have count = 0
    # If there exists empty blobs, their count should be 1
    # e.g., "abc"||"kkk" where the second blob is empty string ===> result = 0|1|0|1
    if not pattern:
        for blob in blobs:
            if not blob:
                result += str(1) + "|"
                total += 1
            else:
                result += str(0) + "|"

        result += str(total)
        return result

    # CASE 2: non-empty pattern
    # Checking each blob bor pattern matching
    for blob in blobs:
        # count is the matches for the blob in question
        # idx is the starting index of the pattern in the blob
        count, idx = 0, 0

        # Until there is no match
        while blob.find(pattern, idx) != -1:
            count += 1
            # Check for pattern starting from the next index
            idx = blob.find(pattern, idx) + 1

        total += count
        result += str(count) + "|"

    # Append the total number of matches to the result
    result += str(total)
    return result


for line in sys.stdin:
    splitted_input = line.split(';')
    pattern = splitted_input[0]

    # Note that I changed a small thing here.
    # Instead of splitting "splitted_input[1]", I'm splitting "splitted_input[1][:-1]" omitting the last char
    # This is bc, in std input, in order to go to the next line, we press return, which adds "\n" as a char to the end
    # Not omitting "\n" would only affect 1 edge case where the last blob is an empty string.
    # e.g., let pattern be an empty set and blobs be "a|", consisting of "a" and empty set "".
    # and ";a|" should return "0|1|1" because the second blob is empty and the pattern is also empty.
    # But if we do not omit the last "\n" , our result would instead be "0|0|0", which is falsely assuming the second
    # blob is non-empty even though it's empty.
    blobs = splitted_input[1][:-1].split('|')

    result = doSomething(blobs, pattern)
    print(result)
