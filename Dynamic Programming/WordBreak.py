def wordBreak(s, wordDict):
    n = len(s)

    # Base case: empty string is a valid word!
    F = [True]

    # List holding the indices at which F[i] = TRUE
    valid_indices = [0]

    for i in range(1, n + 1):
        F.append(False)

    for i in range(1, n + 1):
        for w in valid_indices:
            if F[w] and (s[w : i] in wordDict):
                F[i] = True
                valid_indices.append(i)
                break

    return F[n]



print(wordBreak("dogscat", ['cat', 'cats', 'and', 'dog', 'dogs']))