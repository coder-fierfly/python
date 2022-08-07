def square_sum(a):
    num = float(0)
    for i in a:
        print(type(i))
        num = num + i ** 2
        print(str(num))
    return num
print(square_sum(18, 11, 12, -11, -15))

def sum_array(a):
    sum = float(0)
    for i in a:
        sum += i
    return sum