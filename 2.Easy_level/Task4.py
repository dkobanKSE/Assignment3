list_of_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

summa_num_div_of_y = 0

num_Y = int(input("Введіть ваше число Y: "))

for el in list_of_numbers: 
    if el % num_Y == 0: 
        summa_num_div_of_y += el
        
print(f'Сума чисел, що діляться на Y - {summa_num_div_of_y}')