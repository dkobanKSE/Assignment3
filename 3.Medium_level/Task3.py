str_up = " "

list_of_str = ['ssaad', 'DSadad', 'dsddSSa', 'ssadAsAasAd', 'dsPaOdsa', 'dsDdssFad', 'dGGsHdKadas', 'sOsadop']


for i in range(0, len(list_of_str)): 
    str_low = " "
    
    for char in list_of_str[i]: 
        if char.isupper():
            str_up += char
            
        else:     
            str_low += char
            list_of_str[i] = str_low

print(f'Всі великі літери - {str_up}')
print(f'Список без великих літер - {list_of_str}')