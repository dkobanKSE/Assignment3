list_of_lists_str = [['ssaad', 'DSadad'], ['dsddSSa'] , ['ssadAsAasAd', 'dsPaOdsa'], ['dsDdssFad', 'dGGsHdKadas'], ['sOsadop']]

lenght = len(list_of_lists_str)

for i in range(0, lenght):
    for el in list_of_lists_str[i]:
        list_of_lists_str.append(el)
        
ind = 0 
      
while ind <= lenght:
    if type(list_of_lists_str[ind]) == list:
        list_of_lists_str.pop(ind)
    else: 
        ind += 1
        
print(list_of_lists_str)