# Задача "Счётчик вызовов".
calls = 0
from functools import wraps

def countcall(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        global calls
        calls += 1
        wrapper.count += 1
        result = func(*args, **kwargs)
        return result
    wrapper.count = 0
    return wrapper

@countcall
def string_info(string):
    print((len(string), string.upper(), string.lower()))

@countcall
def is_contains(string, list_to_search):
    list_to_search = ''.join(map(str, list_to_search))
    print(string.lower() in list_to_search.lower())

string_info('Capybara')
string_info('Armageddon')
is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
is_contains('cycle', ['recycling', 'cyclic'])
print(calls)