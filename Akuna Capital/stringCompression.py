def compress(word):
    anchor = write = 0
    chars = []
    chars[:0] = word

    for i in range(len(chars)):
        if i == len(chars) - 1 or chars[i] != chars[i + 1]:
            chars[write] = chars[anchor]
            write += 1
            if i > anchor:
                for digit in str(i - anchor + 1):
                    chars[write] = digit
                    write += 1
            anchor = i + 1

    return "".join(chars[:write])


print(compress("jkllk"))
