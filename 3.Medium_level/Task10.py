list_of_integers_task10 =  [1, 3, 4, 6, 6, 3, 3, 2, 8, 9, 10, 22, 11, -1, 0]

num_X = int(input('Введіть число X - '))
num_Y = int(input('Введіть число Y - '))


for i in range(0, len(list_of_integers_task10)):
    if list_of_integers_task10[i] > num_X:
        list_of_integers_task10[i] = list_of_integers_task10[i] * num_Y
        
print(f'Помножені числа на Y, якщо вони більші за X - {list_of_integers_task10}')