import random

print('Угадайте загаданное число от 0 до 100')
minNum = 0
maxNum = 100
randNum = random.randint(0, 100)
attempts = 1
print('читы: ' + str(randNum))

'''
if num == 'alexcpu7':
    minNum = input('Введите минимальное число: ')
    maxNum = input('Введите максимальное число: ')
'''

while True:
    num = int(input('Введите число: '))
    if num > randNum:
        print('Не верно, чило должно быть ниже\n')
        attempts += 1
    elif num < randNum:
        print('Не верно, чило должно быть выше\n')
        attempts += 1
    else:
        break


print('Поздравляю! Вы отгадали загаданное число c ' + str(attempts) + ' попытки')
