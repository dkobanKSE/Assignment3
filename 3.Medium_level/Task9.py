first_list_str = ['sasasas', 'ds', 'dsdadkas', 'mklmnfks', 'skmlmkadmaa', 'dmskladlas']
second_list_str = ['sasasas', 'ds', 'dsdadkas', 'mklmnfks', 'skmlmkadmaa', 'dmskladlas']

for i in range(0, len(second_list_str)): 
    first_list_str[i] += second_list_str[i]
    
    
print(f'Обєднані рядки по черзі з двох списків - {first_list_str}')