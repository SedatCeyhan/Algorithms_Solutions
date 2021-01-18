def intToRoman(num):

    romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    digits = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    sol = ""
    rom = 0
    while num > 0:
        if digits[rom] <= num:
            count = int(num/digits[rom])
            sol += romans[rom] * count
            num = num % digits[rom]

        rom += 1

    return sol


#print(intToRoman(9))


def romanToInt(roman):

    roman_to_nums = {"M":1000, "CM":900, "D":500, "CD":400,
                     "C":100, "XC":90, "L":50, "XL":40, "X":10, "IX":9, "V":5, "IV":4, "I":1}

    number = 0
    r = 0
    while r < len(roman):
        if r <= len(roman) - 2 and roman[r : r + 2] in roman_to_nums:
            number += roman_to_nums[roman[r : r + 2]]
            r += 2
        else:
            number += roman_to_nums[roman[r]]
            r += 1

    return number

print(romanToInt("CMLX"))
