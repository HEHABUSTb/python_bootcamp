rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

player_choose = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors: "))
computer_choose = random.randint(0, 2)

if player_choose not in [0, 1, 2]:
    print('Type valid number. You lose')
else:

    images = [rock, paper, scissors]
    print(images[player_choose])
    print("Computer chose:")
    print(images[computer_choose])

    if player_choose == computer_choose:
        print('Draw')
    elif player_choose == 0 and computer_choose == 2:
        print('Player win!')
    elif player_choose == 0 and computer_choose == 1:
        print('Computer win!')
    elif player_choose == 1 and computer_choose == 2:
        print('Computer win!')
    elif player_choose == 1 and computer_choose == 0:
        print('Player win!')
    elif player_choose == 2 and computer_choose == 1:
        print('Player win!')
    elif player_choose == 2 and computer_choose == 0:
        print('Computer win!')
