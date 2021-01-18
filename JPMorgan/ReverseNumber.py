def reverse(x):
    if not x: return x

    if x > 0:
        if str(x)[-1] == '0':
            reversed = int(str(x)[:-1][::-1])
            return reversed if reversed < (2**31) - 1 else 0

        reversed = int(str(x)[::-1])
        return reversed if reversed < (2 ** 31) - 1 else 0
    elif x < 0:
        if str(x)[-1] == '0':
            reversed = -int(str(x)[1:-1][::-1])
            return reversed if reversed >= -(2 ** 31) else 0

        reversed = -int(str(x)[1:][::-1])
        return reversed if reversed >= -(2 ** 31) else 0
    else: return 0


print(reverse(-150))
