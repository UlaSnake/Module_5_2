class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

# Пример создания объектов и проверки методов
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# Тестирование методов
print(h1)  # Вывод строки для первого дома
print(h2)  # Вывод строки для второго дома

print(len(h1))  # Вывод количества этажей для первого дома
print(len(h2))  # Вывод количества этажей для второго дома