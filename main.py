RED = '\u001b[41m'
GREEN = '\u001b[42m'
YELLOW = '\u001b[43m'
END = '\u001b[0m'

# Вывод флага
print(f'{GREEN}\t{END}{YELLOW}\t\t\t{END}\n{GREEN}\t{END}{YELLOW}\t\t\t{END}\n{GREEN}\t{END}{RED}\t\t\t{END}\n{GREEN}\t{END}{RED}\t\t\t{END}\n')
print(f' \x1b[31m\x1b[1mBenin flag\t{END}')
# Задание 2 с узором
BLACK = '\u001b[40m'
for i in range(15):
    print(f'{" " * (14-i)}{GREEN}{" " * 2 * i}{END}')
for i in range(14, 0, -1):
    print(f'{" " * (14-i)}{GREEN}{" " * 2 * i}{END}')
# Задание 3 с графиком
plot_list = [[0 for i in range(10)] for i in range(10)]
result = [0 for i in range(10)]

for i in range(10):
    result[i] = i + 1

step = round(abs(result[0] - result[9]) / 9, 2)
print(step)

for i in range(10):
    for j in range(10):
        if j == 0:
            plot_list[i][j] = step * (8-i) + step

for i in range(9):
    for j in range(10):
        if abs(plot_list[i][0] - result[9 - j]) < step:
            for k in range(9):
                if 8 - k == j:
                    plot_list[i][k+1] = 1

for i in range(9):
    line = ''
    for j in range(10):
        if j == 0:
            line += '\t' + str(int(plot_list[i][j])) + '\t'
        if plot_list[i][j] == 0:
            line += '--'
        if plot_list[i][j] == 1:
            line += '!!'
    print(line)
print('\t0\t1 2 3 4 5 6 7 8 9')
# Задание 4 с данными
file = open('sequence.txt', 'r')
list = []
numb1 = numb2 = 0
for number in file:
    list.append(float(number))
file.close()
for i in range(len(list)):
    if -5 < list[i] < 0:
        numb1 += 1
    if list[i] < -5:
        numb2 += 1
percent1 = round(numb1/(numb1+numb2)*100, 2)
percent2 = round(numb2/(numb1+numb2)*100, 2)
print("Числа большие -5, но меньшие 0", "[", numb1, "]")
print(f'{RED}{" " * numb1}{END}{percent1}{"%"}')
print("Числа меньшие -5", "[", numb2, "]")
print(f'{GREEN}{" " * numb2}{END}{percent2}{"%"}')
