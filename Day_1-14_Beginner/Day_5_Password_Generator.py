# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
def easy_password(nr_letters, nr_numbers, nr_symbols):
    password = ''
    for i in range(0, nr_letters):
        upper = random.randint(0, 1)
        random.shuffle(letters)
        if upper == 1:
            password += letters[0].upper()
        if upper == 0:
            password += letters[0]

    for i in range(0, nr_numbers):
        random.shuffle(numbers)
        password += numbers[0]

    for i in range(0, nr_symbols):
        random.shuffle(symbols)
        password += symbols[0]
    return password


password = easy_password(nr_letters, nr_numbers, nr_symbols)
print(password)

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


class PasswordGenerator:
    def __init__(self, nr_letters, nr_numbers, nr_symbols):
        self.nr_letters = nr_letters
        self.nr_numbers = nr_numbers
        self.nr_symbols = nr_symbols
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                   'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    def add_letter(self, password: list):
        upper = random.randint(0, 1)
        random.shuffle(self.letters)
        if upper == 1:
            password.append(self.letters[0].upper())
        if upper == 0:
            password.append(self.letters[0])

        return password

    def add_number(self, password: list):
        random.shuffle(self.numbers)
        password.append(self.numbers[0])

        return password

    def add_symbols(self, password: list):
        random.shuffle(self.symbols)
        password.append(self.symbols[0])

        return password

    def shuffle_password(self, password: list):

        shuffled = ''
        for i in range(0, len(password)):
            letter = random.choice(password)
            password.remove(letter)
            shuffled += letter
        return shuffled

    def hard_password(self):
        password = []
        for i in range(0, self.nr_letters):
            self.add_letter(password)
        for i in range(0, self.nr_numbers):
            self.add_number(password)
        for i in range(0, self.nr_symbols):
            self.add_symbols(password)

        return self.shuffle_password(password)


password_generator = PasswordGenerator(nr_letters, nr_numbers, nr_symbols)
password = password_generator.hard_password()
print(password)

