cities = [
    'Москва',
    'Токио',
    'Париж',
    'Нью-Йорк',
    'Лондон',
    'Берлин',
    'Сингапур',
    'Копенгаген',
    'Амстердам',
    'Сидней'
]

# TODO с помощью цикла for и команды enumerate распечатайте рейтинг городов
for i in enumerate(cities, start=1):
    print(f"{i[0]:2}-е место: {i[1]}")