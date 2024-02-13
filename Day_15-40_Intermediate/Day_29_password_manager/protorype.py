import csv
import random

def save(website: str, username: str, password: str, mode='a'):
    # Set mode='w' if you want to rewrite file
    header = ['website', 'username', 'password']
    data = [website, username, password]

    with open('secret.csv', mode, newline='') as file:
        writer = csv.writer(file)
        if mode == 'w':
            writer.writerow(header)
        writer.writerow(data)



def password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    password_list += [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    print(password_list)

    random.shuffle(password_list)

    password = "".join(password_list)

    print(f"Your password is: {password}")

password()