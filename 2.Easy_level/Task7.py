list_of_string = ['ssadsd', 'dgkfog', 'gifojx', 'wiqeoq', 'iissii', 'qkpol', 'oqp', 'ssa', 'sas']

prefics_str = str(input('Введіть ваш префікс: '))

print(f'Елемент, що починаються з {prefics_str} - ', end = '')

for el in list_of_string: 
    if el.startswith(prefics_str):
        print(el, end = ' ')