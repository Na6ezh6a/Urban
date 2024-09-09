#Работа со словарями:
my_dict = {'Moon': 2024, 'Alexander': 2000}
print('Dict:', my_dict)
print('Existing value:', my_dict['Moon'])
print(my_dict.get('Hope', 'Not existing value.'))  #Вывести на экран одно значение по отсутствующему из словаря my_dict без ошибки.
my_dict.update({'Denis': 1997,
                'Olya': 1999})
print('Modified dictionary:', my_dict)
a = my_dict.pop('Denis')
print('Deleted value:', a)
print('New modified dictionary:', my_dict)

#Работа с множествами:
my_set = {'Doberman', 21, False, (9, 19, 21), 21, True}
print('Set:', my_set)
my_set.update({'Moon', 19})     #Добавить сразу несколько элементов в множество.
my_set.add(3)                   #Добавить один элемент в множество.
my_set.discard(True)            #Удалить один любой элемент из множества.
print('Modified set:', my_set)