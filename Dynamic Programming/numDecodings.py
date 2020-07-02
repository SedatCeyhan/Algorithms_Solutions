def numDecodings(s):

    if len(s) == 0: return 0

    n = len(s)
    F = []

    # Base case: Empty string has no decoding
    for i in range(n + 1):
        F.append(0)

    # 1 digit number can have only 1 letter ==> single decoding
    if s[0] == '0':
        return 0

    F[1] = 1

    # No real reasonning -> if nothing provided only one way to decode, no way
    F[0] = 1


    for i in range(2, n + 1):
        if s[i - 1] == "0" and s[i - 2] == "0": return 0

        if s[i - 1] == "0":
            if int(s[i - 2 : i]) <= 26:
                F[i] = F[i - 2]
            else: return 0

        elif int(s[i - 2 : i]) > 26 or s[i - 2] == "0":
            F[i] = F[i - 1]
        else:
            F[i] = F[i - 1] + F[i - 2]

    return F[n]

print(numDecodings("123"))

