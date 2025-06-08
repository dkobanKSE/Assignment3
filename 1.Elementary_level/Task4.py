list_of_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Непарні числа в списку - ", end = ' ')
for el in list_of_numbers: 
    if el % 2 != 0: 
        print(el, end = ' ')