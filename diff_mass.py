def array_diff(a, b):
    c = []
    for i in a:
        if not (i in b):
            c.append(i)
    return c

# def array_diff(a, b):
#     return [x for x in a if x not in b]