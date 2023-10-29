city_list = [
    {"city": "Москва", "population": 12.5},
    {"city": "Санкт-Петербург", "population": 5.4},
    {"city": "Москва", "population": 1.6},
    {"city": "Екатеринбург", "population": 1.5},
    {"city": "Нижний Новгород", "population": 1.3},
]

population_list = [x['population'] for x in city_list ]
average_population = sum(population_list)/len(population_list)

print(f"Среднее арифметическое населения равно = {average_population}")  # TODO распечатайте среднее арифметическое населения
