def reverseString(line):
    solution = ""  # Solution string with capitalized words
    line = line.split()  # List of words in a given line separated by commas
    for word in line:
        solution += word[0].upper() + word[1:] + " "
    return solution[:-1]

print(reverseString("hey       ,, my name is sedat!"))


