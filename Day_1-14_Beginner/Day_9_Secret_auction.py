from Day_9_art import logo

#HINT: You can call clear() to clear the output in the console.
from replit import clear


def find_winner(bids):
    winner = {}
    high_score = 0
    for key in bids:
        if key['bind'] > high_score:
            high_score = key['bind']
            winner = {'name': key['name'], 'bind': key['bind']}
    return winner

print(logo)

bids = []
terminate_program = False


while terminate_program is False:

    name = input('Type name \n')
    bind = int(input('Type bind \n'))

    bids.append({'name': name, 'bind': bind})

    next = input("Do you wanna continue 'yes' or 'no'\n")
    next = next.lower()

    if next == 'yes':
        clear()
    elif next == 'no':
        winner = find_winner(bids)
        print(f"Winner is '{winner['name']}' with bed ${winner['bind']}")

        terminate_program = True

