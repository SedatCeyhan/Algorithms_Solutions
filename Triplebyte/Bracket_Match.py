def bracket_match(bracket_string):
    # Number of "(" encountered
    left = 0
    # Required number of additions of either "(" or ")"
    required = 0

    for paran in bracket_string:
        if paran == "(": left += 1
        else: left -= 1

        # Any time we have more ")" than "(", close the parentheses
        # by adding additional left parenthese - "("
        # Thus left ++; required ++
        if left < 0:
            left += 1
            required += 1

    # if we still have more left than right, add left many right parentheses
    # to make the string valid
    if left > 0: return required + left

    # Already fixed in the loop
    return required


print(bracket_match(""))