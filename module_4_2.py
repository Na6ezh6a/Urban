def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()
# Вызываем функцию inner_function внутри функции test_function (1-ый вариант).
test_function()

# Вызываем функцию inner_function внутри функции test_function (2-ой вариант).
if __name__ == "__main__":
    test_function()
# Вызываем функцию inner_function вне функции test_function.
try:
    inner_function()  # Это вызовет ошибку.
except NameError as e:
    print(f"Ошибка: {e}")  # Печатаем сообщение об ошибке.