def count_by(x, n):
    i = 1
    y = 1
    mass = []
    while y <= n:
        if (i % x == 0):
            mass.append(i)
            y += 1
        i += 1
    return mass
print(count_by(2,5))

# def count_by(x, n):
#     return [i * x for i in range(1, n + 1)]
