import re
# Программа берет математическое выражение из файла input.txt, записывает результат в файл output.txt
input = open("input.txt", "r")
output = open("output.txt", "w")
for line in input:
    line = line.replace('\n', '')
    # addition
    if re.fullmatch(r"\d+\+\d+", line):
        a, b = line.split('+')
        output.write(line + ' = ' + str(float(a)+float(b)) + '\n')
    # subtraction
    elif re.fullmatch(r"\d+\-\d+", line):
        a, b = line.split('-')
        output.write(line + ' = ' + str(float(a)-float(b)) + '\n')
    # multiplication
    elif re.fullmatch(r"\d+\*\d+", line):
        a, b = line.split('*')
        output.write(line + ' = ' + str(float(a) * float(b)) + '\n')
    # division
    elif re.fullmatch(r"\d+/\d+", line):
        a, b = line.split('/')
        output.write(line + ' = ' + str(float(a) / float(b)) + '\n')
    else:
        output.write("error: all format string" + '\n')