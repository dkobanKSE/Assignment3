list_of_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

num_x = int(input("Введіть ваше числo X: "))

print(f'Числа більші за X - ', end = '')

for el in list_of_numbers: 
    if el > num_x: 
        print(el, end = ' ')
                
