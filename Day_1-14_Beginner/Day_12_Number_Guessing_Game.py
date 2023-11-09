import random


def int_input(message: str):
    loop = True
    while loop:
        answer = input(message)
        if answer.isdigit():
            answer = int(answer)
            if 0 < answer < 101:
                loop = False
                return int(answer)
            else:
                print(f'Number should be between 1 and 100 not {answer}')
        else:
            print('It should be a digit')

def lose_message(attempt: int, ai_number: int, text = 'You lose!'):
    if attempt == 0:
        print(f"{text}: AI number was {ai_number}")

def game():

    print(f"I'm thinking of a number between 1 and 100")
    ai_number = random.randint(1, 100)
    print(f'Number: {ai_number}')

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    attempt = int

    if difficulty == 'easy':
        attempt = 15
    elif difficulty == 'hard':
        attempt = 10

    while attempt > 0:
        print(f"You have {attempt} attempts remaining to guess the number")
        player_number = int_input(f"Make a guess: ")

        if player_number > ai_number:
            print(f'Too high')
            attempt -= 1
            lose_message(attempt=attempt, ai_number=ai_number)
        elif player_number < ai_number:
            print(f"Too low")
            attempt -= 1
            lose_message(attempt=attempt, ai_number=ai_number)
        elif player_number == ai_number:
            print(f'You win !')
            attempt = 0
        else:
            print(f"Unexpected result ai_number {ai_number} player_number {player_number}")

game()
