list_of_numbers = [0, 1, 2, 3, -4, 5, 6, 7, 8, 9, 10]

num_n = int(input('Введіть число N: '))
sum_of_n_nums = 0

for el in list_of_numbers[:num_n]:
    sum_of_n_nums += el
    
print(f'Сума перших N чисел в списку - {sum_of_n_nums}')