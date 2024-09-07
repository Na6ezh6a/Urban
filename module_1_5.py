immutable_var = "Hope", 19, True
print("Immutable tuple:", immutable_var)
# immutable_var[1] = 21
# Кортеж является неизменяемым типом.
# Поэтому мы не можем добавлять или удалять элементы в кортеже, изменять его.

mutable_list = ["Hope", 19, False, 21]
print("Mutable list:", mutable_list)
mutable_list[0:3] = [True, 3, "Moon"]
print("New Mutable list:", mutable_list)

