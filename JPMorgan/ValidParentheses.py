def isValid(s):

    map = {'[':']', '{':'}', '(':')'}
    stack = []

    for paren in s:
        # If it's a left parenthese, add it to our stack
        if paren in map:
            stack.append(paren)

        # It's a right parenthese
        else:
            # If stack is empty, there is NO left parenthese to match the current right parenthese
            if not stack: return False
            # the very previous left parenthese must be of similar type
            # e.g., '{' for '}'
            elif map[stack.pop()] != paren: return False

    return not stack


print(isValid("()[]"))