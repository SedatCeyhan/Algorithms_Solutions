def secretFruitList(codeList, shoppingCart):
    if not codeList: return 1
    if not shoppingCart: return 0

    i, j = 0, 0
    while i < len(codeList):
        if j + len(codeList[i]) > len(shoppingCart): return 0
        match = True
        for k in range(len(codeList[i])):
            if codeList[i][k] != "anything" and codeList[i][k] != shoppingCart[j]:
                match = False
                break

        if not match:
            j += 1
        else:
            j += len(codeList[i])
            i += 1

    return 1



# Input: codeList = [[apple, apple], [banana, anything, banana]]
# shoppingCart = [banana, orange, banana, apple, apple]
print(secretFruitList([["apple", "apple"], ["banana", "anything", "banana"]], ["banana", "orange", "banana", "apple", "apple"]))