import random, os
from Art.Day_14_Art import logo, vs
from Art.Day_14_Data import data

clear = lambda: os.system('cls')


def choose_blogers(quantity: int, bloggers: list):
    global data
    for i in range(0, quantity):
        len_data = len(data) - 1
        random_index = random.randint(0, len_data)

        data_a = data.pop(random_index)
        bloggers.append(data_a)


def choose_winner(a: dict, b: dict):
    if a['number'] > b['number']:
        return 'A'
    elif a['number'] < b['number']:
        return 'B'
    elif a['number'] == b['number']:
        return 'same'
    else:
        print(f'Something go wrong check the data {a} and {b}')


def game():
    print(logo)

    game_data = data
    bloggers = []
    running = True
    final_score = 0
    while running:

        if final_score > 0:
            print("--------------------------------------------------------------------------------------------------------------------------")
            print(f"Ты прав! Угадал {final_score} раз. У {compare_a['name']} - {compare_a['subscribers']}, а {compare_b['name']} имеет {compare_b['subscribers']}   ")
        # We need to check that list have more than 1 data
        len_data = len(game_data)
        if len_data < 2:
            print('Список закончился, ты лучший знаток.')
            running = False
            break
        # We find and take blogger to bloggers
        if final_score == 0:
            choose_blogers(2, bloggers)
        else:
            choose_blogers(1, bloggers)


        compare_a = bloggers[0]
        compare_b = bloggers[1]
        print(f"Сравни А: {compare_a['name']} - {compare_a['description']}.")
        print(vs)
        print(f"Против B: {compare_b['name']} - {compare_b['description']}.")

        # Нужно проверить буквы
        answer = input("У кого больше подписчиков? Введи А или B: ")

        winner = choose_winner(compare_a, compare_b)
        if winner == answer or winner == 'same':
            final_score += 1
            clear()
            if answer == 'A':
                bloggers.remove(compare_b)
            elif answer == 'B':
                bloggers.remove(compare_a)

        else:
            print(f"Ты ошибся! У {compare_a['name']} - {compare_a['subscribers']}, а {compare_b['name']} имеет {compare_b['subscribers']}")
            # Хочешь ли продолжить
            answer = input("Хочешь начать ещё раз ? Y or N: ")
            if answer == 'Y' or answer == 'y':
                game()
            else:
                running = False


game()