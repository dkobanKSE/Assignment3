list_of_string = ['ssadsd', 'dgkfog', 'gifojx', 'ii', 'wiqeoq', 'iissii', 'qkpol', 'oqp', 'ssa', 'sas']


list_of_polindroms = [] 

for el in list_of_string: 
    if el == el[::-1]:
        list_of_polindroms.append(el)
        
print(f'Список поліндромів - {list_of_polindroms}')