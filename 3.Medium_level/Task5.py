cond_list_1 = ['ssasa', 'dsdssa', 382, False, True, 'dsds', 3.4]
cond_list_2 = ['asssa', 'dsdsadsadasdsa', 323, True, True,'sas', 3.2]
cond_list = []

if len(cond_list_1) == len(cond_list_2): 
    for i in range(0, len(cond_list_1)):
        if type(cond_list_1[i]) == type(cond_list_2[i]):
            cond_list.append(cond_list_1[i])
            cond_list.append(cond_list_2[i])
            
        else:
            print("Списки не відповідають умовам")
            break

print(f'Обєднаний список за умовою - {cond_list}')