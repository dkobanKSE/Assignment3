list_of_integers =  [1, 3, 4, 6, 6, 3, 3, 2, 8, 9, 10, 22, 11, -1, 0]

list_of_integers.sort(reverse=True)


for i in range(0, len(list_of_integers)): 
    j = i + 1
    
    for ind in range(j, len(list_of_integers)):
        if list_of_integers[i] == list_of_integers[ind]:
            list_of_integers[i+1], list_of_integers[ind] = list_of_integers[ind], list_of_integers[i+1]
    

print(list_of_integers)