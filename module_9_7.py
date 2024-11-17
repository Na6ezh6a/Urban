# Задание: Декораторы в Python.
def sum_three(a, b, c):
    return a + b + c
def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result > 1:
            if (result % 2 != 0 or result == 2) and (result % 3 != 0 or result == 3):
                print("Простое")
            else:
                print("Составное")
        return result
    return wrapper
@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)


