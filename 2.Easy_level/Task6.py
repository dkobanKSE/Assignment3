list_of_numbers = [0, 1, 2, 3, -4, 5, 6, 7, 8, 9, 10]

list_of_pos_num = []

for el in list_of_numbers:
    if el > 0: 
        list_of_pos_num.append(el)
        
print(f'Список додатних чисел - {list_of_pos_num}')