'''перебор массива 1'''
mas = list(range(10))

print(mas)

i = 0
length = len(mas)

while i < length:
    print(mas[i])
    i += 1


'''перебор массива 2'''
mas = [1, 2, 3, 4, 5]

for item in mas:
    print(item)


'''вывести 10 раз'''
for i in range(10):
    print(10)


'''функции'''
def fun():
    print('This my function!!!')

fun()

# передача функции (ВНИМАНИЕ) в функцию

def hawdy_ho(name):
    print('My name is ' + name())

def read_name():
    return input('Введите ваше имя: ')

hawdy_ho(read_name)