list_of_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

suma_numlist = 0
count_pos_num = 0

for el in list_of_numbers:
    if el > 0: 
        suma_numlist += el
        count_pos_num += 1
        
print(f'Середнє додатних чисел - {suma_numlist/count_pos_num}.') 