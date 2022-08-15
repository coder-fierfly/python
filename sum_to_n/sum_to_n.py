# Требуется посчитать сумму целых чисел, расположенных между числами 1 и N включительно.
input = open("input.txt", "r")
output = open("output.txt", "w")

sum = 0
for line in input:
    num = int(line)
    if num>0:
        for i in range(1, num + 1):
           sum += i
    else:
        for i in range(num, 2):
           sum += i

output.write(str(sum))