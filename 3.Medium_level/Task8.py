#№8
list_of_string_grt_X = ['4423', '32dsadsd', 'dadsdfs', 'dadkadas', 'dfmskfnsk', 'cdlksksckds', 'fmkldsmfdksfmsd', '']

len_of_str_X = int(input("Введіть ваше число - "))
amount_of_strs = 0

for el in list_of_string_grt_X:
    if len(el) > len_of_str_X: 
        amount_of_strs += 1
        
print(f'Кількість рядків довші за X - {amount_of_strs}')