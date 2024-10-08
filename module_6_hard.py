# Задание "Они все так похожи".
import math
class Figure:
    sides_count = 0
    def __init__(self, color, *sides):
        self.__sides = self.__initialize_sides(sides)
        self.__color = list(color)
        self.filled = False
    def __initialize_sides(self, sides):
        if len(sides) == self.sides_count:
            return list(sides)
        return [1] * self.sides_count
    def get_color(self):
        return self.__color
    def __is_valid_color(self, r, g, b):
        return all(0 <= x <= 255 for x in (r, g, b)) and all(isinstance(x, int) for x in (r, g, b))
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
    def __is_valid_sides(self, *new_sides):
        return len(new_sides) == self.sides_count and all(isinstance(x, int) and x > 0 for x in new_sides)
    def get_sides(self):
        return self.__sides
    def __len__(self):
        return sum(self.__sides)
    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
class Circle(Figure):
    sides_count = 1
    def __init__(self, color, length):
        super().__init__(color, length)
        self.__radius = length / (2 * math.pi)     # Радиус круга.
    def get_square(self):
        return math.pi * self.__radius ** 2        # Площадь круга.
class Triangle(Figure):
    sides_count = 3
    # Формула Герона (площадь треугольника).
    def get_square(self):
        a, b, c = self.__sides
        p = sum(self.__sides) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5
class Cube(Figure):
    sides_count = 12
    def __init__(self, color,  *sides: int, filled: bool = True):
        super().__init__(color, *sides, filled)
        if len(sides) == 1:
            self.__sides = self.sides_count * [i for i in sides]
        else:
            self.__sides = [1 * self.sides_count]

    def get_sides(self):
        return [*self.__sides]

    def get_volume(self):
        return self.__sides[1]**3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
