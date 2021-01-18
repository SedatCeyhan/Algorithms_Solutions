def push(value, result=[]):
    result.append(value)
    return result


first = push(0)
push(1, first)
print(push(2))