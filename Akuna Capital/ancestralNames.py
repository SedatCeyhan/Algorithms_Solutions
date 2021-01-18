def romanToInt(roman):
    roman_to_nums = {"M": 1000, "CM": 900, "D": 500, "CD": 400,
                     "C": 100, "XC": 90, "L": 50, "XL": 40,
                     "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}
    number = 0
    r = 0
    while r < len(roman):
        if r <= len(roman) - 2 and roman[r: r + 2] in roman_to_nums:
            number += roman_to_nums[roman[r: r + 2]]
            r += 2
        else:
            number += roman_to_nums[roman[r]]
            r += 1

    return number


def sortRoman(names):
    return sorted(names, key=lambda  name: (name.split()[0], romanToInt(name.split()[1])))


print(sortRoman(["Steven XL", "Steven XVI", "David IX", "Mary XV", "Mary XIII", "Mary XX"]))