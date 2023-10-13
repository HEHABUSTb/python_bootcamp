import random
from Art.Day_7_Pictures import stages, logo, word_list


# Functions
def check_player_win(word: list):
    if "_" not in word:
        return True
    else:
        return False


def check_player_input(player_input: str, player_input_set: set, hidden_word: list):
    if len(player_input) == 1 and player_input.isalpha() is True:
        # print(f'Your letter: {player_input}')
        if player_input in player_input_set:
            print(f'You already try this letter {player_input}, {player_input_set}\n{hidden_word}')
            return False
        return True
    else:
        return False


# Step Randomly choose a word
print(logo)
chosen_word = random.choice(word_list)
# print(f'Chosen word ', chosen_word)

# Step For each letter in the chosen_word, add a "_" to 'display'.
hidden_word = []
for letter in chosen_word:
    hidden_word.append('_')

# Step  Ask user to guess a letter and assign answer

player_input = ''
player_input_set = {''}
end_game = False
lifes = 6

print(hidden_word, "\n", stages[lifes])


while end_game is False:
    player_input = input(f'Your guess? \n')
    player_input = player_input.lower()

    # checking input is valid
    if check_player_input(player_input, player_input_set, hidden_word) is True:
        player_input_set.add(player_input)

        # checking letter in hidden word
        word_len = len(chosen_word)

        if player_input in chosen_word:
            for position in range(word_len):
                if chosen_word[position] == player_input:
                    hidden_word[position] = chosen_word[position]
            print(hidden_word, '\n', stages[lifes])
        else:
            lifes -= 1
            print('Yoy are wrong !', '\n', hidden_word, stages[lifes])
            if lifes == 0:
                print('You lose the game !\n', 'Word was', chosen_word)
                end_game = True
        if '_' not in hidden_word:
            print('You win!')
            end_game = True
