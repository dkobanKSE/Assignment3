#№6 
marks_dict = [
        {'Предмет': "OIT", 'Оцінка': 45},
        {'Предмет': "VMA", 'Оцінка': 67},
        {'Предмет': "OP" ,'Оцінка': 90},
        {'Предмет': "HoU" ,'Оцінка': 87},
        {'Предмет': "OIT" ,'Оцінка': 43}
        ]

sum_of_marks = 0
subject = str(input("Напишіть ваш предмет - "))

for el in marks_dict:
    if el['Предмет'] == subject:
        sum_of_marks += el['Оцінка']
    
print(f'Сума всіх оцінок по предмету - {sum_of_marks}')