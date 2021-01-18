def numDecodings(line):
    if not line: return 0
    n = len(line)
    dp = [0] * (n + 1)

    # Base Cases:
    dp[0] = 1

    if line[0] == "0": return 0
    dp[1] = 1

    for i in range(2, n + 1):
        '''
        e.g., we previously had something like '220' (only way to decode 2 + 20)
        but if the next digit is also '0', then we have '2200' ==> invalid input for decoding
        '''
        if line[i - 2:i] == "00":
            return 0

        # Similar to previous case, the next digit is a '0', but the previous was NOT a '0'
        elif line[i - 1] == "0":
            # e.g., the last two digits we have is either '10' or '20'
            # We can not decode the last '0' as an individual letter, so we consider last 2 digits (10 or 20)
            # as a separate letter. Thus the possibilities at index = i is the same as at index = i - 2
            if int(line[i - 2:i]) <= 26:
                dp[i] = dp[i - 2]

            # We got last 2 digits > 26 with the last digit = 0 (e.g., 50). In this case, no way to decode
            else:
                return 0

        # The current digit is NOT a '0' and we have no '00' as our last 2 digits
        else:
            # Case where the last two digits are something like e.g., '05' or '37'.
            # In either case, we cannot consider the last two digit to be an individual letter so
            # the only option is to have the current digit to be a letter itself so
            # the possibilities at index = i is the same as at index = i - 1
            if line[i - 2] == "0" or int(line[i - 2:i]) > 26:
                dp[i] = dp[i - 1]
            # Neither the current digit nor the previous one are '0', and the last two digits <= 26 (possible letter)
            # So, first consider the current digit to be an individual letter (dp[i - 1]); then consider the last
            # two digits to be a letter itself (dp[i - 2]) ==> dp[i - 1] + dp[i - 2]
            else:
                dp[i] = dp[i - 1] + dp[i - 2]

    return dp[-1]