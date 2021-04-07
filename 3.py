# Начав тренировки, спортсмен пробежал 10 км. Каждый следующий день он увеличивал
# дневную норму на 10% от нормы предыдущего дня. Какой суммарный путь пробежит спортсмен за 7 дней?

distance = 10
n = 7
for i in range(1, n + 1):
    if i == 1:
        result = distance
    else:
        distance += distance * 0.1
        result += distance
print('{}'.format('%.6f' % result))
