# Задача "Рекурсивное умножение цифр".
def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    str_number = str_number.replace('0', '')
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return int(first)

result = get_multiplied_digits(40203)
print(result)