list_of_cond = [1, 0, -1, 32, -2, 0.5, -13, 32, 0, -21, 1, -7, 'alss']

for i, el in enumerate(list_of_cond):
    
    if type(el) != int and type(el) != float:
        list_of_cond[i] = 'Не число'
        continue
    
    if el < 0: 
        list_of_cond[i] = 'Негативне'
        
    elif el == 0 :
        list_of_cond[i] = 'Нуль'
        
    else:
        list_of_cond[i] = 'Позитивне'
        
    if type(el) != int and type(el) != float:
        list_of_cond[i] = 'Не число'
        
print(f'Список на уснові умов про число - {list_of_cond}')
