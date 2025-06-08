list_of_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num_x = int(input("Введіть ваше число X - "))
num_y = int(input("Введіть ваше число Y - "))

print("Числа, що діляться на Х та не діляться на Y: ", end = '')

for el in list_of_numbers: 
    if el % num_x == 0 and el % num_y != 0: 
        print(el, end = ' ')