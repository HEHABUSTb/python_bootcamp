from Day_3_pictures import print_treasure, print_island

print_island()
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇
choice = input("You\'re at a crossroad, where do you want to go? Type 'left' or 'right': ").lower()

if choice == 'right':
    # Continue game
    pass
else:
    print('You fell into a hole. Game over.')

choice = input("You\'re at a river, what are you want to do? Type 'swim' or 'wait': ").lower()

if choice == 'wait':
    # Continue game
    pass
else:
    print('You fell into a hole. Game over.')

choice = input("You\'re at a door, which door you want to open? Type 'red' or 'blue' or 'yellow': ").lower()

if choice == 'yellow':
    print_treasure()
    print('You find the treasure')
elif choice == 'red':
    print("Burned by fire. Game over.")
elif choice == 'blue':
    print('Eaten by Beast. Game over.')
else:
    print('Wrong input. Game over.')
