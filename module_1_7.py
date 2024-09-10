#Задание "Средний балл":
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]      #Список.
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}                            #Множество.
students = sorted(students)                                                             #Упорядоченное множество.

for i in range(len(grades)):                        #Список средних значений.
    grades[i] = sum(grades[i]) / len(grades[i])

dict = {}                                           #Словарь: имя + ср.знач.
for i in range(len(grades)):
    dict[students[i]] = grades[i]
print(dict)