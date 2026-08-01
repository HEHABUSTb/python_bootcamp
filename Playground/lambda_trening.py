# 1. Дан список чисел. С помощью lambda и map() получи список, где каждое число умножено на 3.
numbers = [1, 2, 3, 4, 5]
# твой код здесь -> [3, 6, 9, 12, 15]

print(list(map(lambda x: x * 3, numbers)))

# 2. Дан список слов. С помощью lambda и filter() оставь только слова длиннее 4 символов.
words = ["кот", "собака", "дом", "автомобиль", "сад"]
# твой код здесь -> ['собака', 'автомобиль']
print(list(filter(lambda  x: len(x) > 4, words)))

# 3 Дан список словарей с товарами. Отсортируй по цене (price) с помощью lambda в key.
products = [
    {"name": "Мышь", "price": 50000},
    {"name": "Клавиатура", "price": 2500},
    {"name": "Клавиатуро", "price": 800},
]

print(sorted(products, key=lambda x: x['price']))

# 4 Тот же список products. Отсортируй сначала по длине имени (name), потом при равенстве — по цене, в порядке убывания цены.
# Подсказка: key может возвращать кортеж, например lambda x: (len(x["name"]), -x["price"])

print(sorted(products, key=lambda x: (len(x['name']), -x['price'])))

# 5 Напиши лямбду label, которая принимает число и возвращает строку:
# "отрицательное", если число меньше 0
# "ноль", если число равно 0
# "положительное", если число больше 0

label = lambda x: "положительное" if  x > 0 else "отрицательное" if x < 0 else "ноль"

print(label(0))
print(label(3))
print(label(-3))

# 6 Дан список чисел от 1 до 20. Получи список квадратов только тех чисел, которые делятся на 3 (используя и filter, и map с лямбдами в одной цепочке).
numbers = list(range(1, 21))
# твой код здесь -> [9, 36, 81, 144, 225, 324]

filtered_numbers = list(filter(lambda x: x % 3 == 0, numbers ))
print(list(map(lambda x: x ** 2, filtered_numbers)))

# 7 С помощью functools.reduce и лямбды найди произведение всех чисел в списке.
from functools import reduce
numbers = [1, 2, 3, 4, 5]
# твой код здесь -> 120
# reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
print(reduce(lambda x, y: x * y, numbers))

result = reduce(lambda acc, x: acc + str(x), [1, 2, 3, 4], "")
print(result)