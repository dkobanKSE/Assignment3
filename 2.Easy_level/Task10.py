list_of_numbers = [0, 1, 2, 3, -4, 5, 6, 7, 8, 9, 10]

list_of_bools = []
num_of_div = int(input("Введіть ваше число: "))

for el in list_of_numbers: 
    if el % num_of_div == 0 and el != 0: 
        list_of_bools.append(True)
    else: 
        list_of_bools.append(False)
    
print(f'Ділять числа на Y - {list_of_bools}')