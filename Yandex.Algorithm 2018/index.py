'''
=== Лотерейный билет ===

На различных мероприятиях команда стажировок регулярно разыгрывает призы в лотерею.

Организаторы выбирают 10 случайных различных чисел от 1 до 32. Каждому участнику выдается лотерейный билет, на котором записаны 6 различных чисел от 1 до 32. Билет считается выигрышным, если в нем есть не менее 3 выбранных организаторами числа.

Помогите Юле, напишите программу, которая будет сообщать, какие билеты выигрышные.

Формат ввода
В первой строке входных данных записаны 10 различных целых чисел ai (1 ≤ ai ≤ 32) — выбранные организаторами числа.

Во второй строке записано одно целое число n (1 ≤ n ≤ 1000) — количество лотерейных билетов, выданных на мероприятии.

В каждой из n последующих строк записаны 6 различных целых чисел bj (1 ≤ bj ≤ 32) — числа, записанные на очередном лотерейном билета.

Формат вывода
Выведите n строк. Для каждого лотерейного билета в порядке следования во входных данных выведите строку Lucky, если билет выигрышный, иначе выведите Unlucky.

Пример
Ввод	                    Вывод
1 2 3 4 5 6 7 8 9 32        Unlucky
3                           Lucky
1 2 10 11 12 13             Lucky
1 2 3 10 11 12
32 1 10 20 30 3

'''


from random import sample

dano = list(map(int, input('Введите 10 различных чисел: ').split()))

tickets = int(input('Введите количество лотерейных билетов: '))

for i in range(tickets):
    allList = list(range(1, 33))
    res = sample(allList, 6)

    filter = lambda x: x in res
    concurrences = [x for x in [y for y in dano if filter(y)]]

    if len(concurrences) >= 3:
        print('Lucky')
    else:
        print('Unlucky')