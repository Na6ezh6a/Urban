my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while index < len(my_list) or index == len(my_list):
    i = index
    if my_list[i] > 0:
        print(my_list[i])
        index += 1
    elif my_list[i] == 0:
        index += 1
    else:
        break
