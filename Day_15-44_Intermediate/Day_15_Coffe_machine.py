from Data.Day_15_menu import MENU, resources


class Coffe:

    def __init__(self):
        self.water = resources["water"]
        self.milk = resources['milk']
        self.coffee = resources['coffee']
        self.MENU = MENU
        self.money = 0

    def input_order(self):
        # Player enter input
        answer = str(input('“What would you like? (espresso/latte/cappuccino): '))
        return answer

    def report(self):
        print(f"Water: {self.water}ml")
        print(f"Milk: {self.milk}ml")
        print(f"Coffee: {self.coffee}g")
        print(f"Money: ${self.money}")

    def check_resources(self, drink: str):
        ingredients = self.MENU[drink]
        i = 0
        for ingredient in ingredients['ingredients']:
            if ingredient == 'water':
                if self.water - ingredients['ingredients'][ingredient] < 0:
                    print(f"Sorry there is not enough water.")
                    i += 1
            elif ingredient == 'coffee':
                if self.coffee - ingredients['ingredients'][ingredient] < 0:
                    print(f"Sorry there is not enough coffee.")
                    i += 1
            elif ingredient == 'milk':
                if self.milk - ingredients['ingredients'][ingredient] < 0:
                    print(f"Sorry there is not enough milk.")
                    i += 1
            if i > 0:
                self.play()

    def minus_ingredients(self, drink):
        ingredients = self.MENU[drink]
        for ingredient in ingredients['ingredients']:
            if ingredient == 'water':
                self.water -= ingredients['ingredients'][ingredient]
            elif ingredient == 'coffee':
                self.coffee -= ingredients['ingredients'][ingredient]
            elif ingredient == 'milk':
                self.milk -= ingredients['ingredients'][ingredient]

    def insert_coins(self, drink: str):

        print(f"Please insert coins")
        cena = self.MENU[drink]['cost']

        summa = 0
        summa += int(input('How many quarters?: ')) * 0.25
        summa += int(input('How many dimes?: ')) * 0.10
        summa += int(input('How many nickels?: ')) * 0.05
        summa += int(input('How many pennies?: ')) * 0.01

        change = summa - cena

        if change >= 0:
            self.money += cena
            print(f"Here is your change ${change:.2f}")
            print(f'Here is your {drink}')
            self.minus_ingredients(drink)
        else:
            print(f'Not enough money!')
            self.play()

    def play(self):
        running = True
        drinks = ['espresso', 'latte', 'cappuccino']
        while running:
            answer = self.input_order()
            if answer == 'report':
                self.report()
            elif answer in drinks:
                self.check_resources(answer)
                self.insert_coins(answer)
            elif answer == 'off':
                running = False


if __name__ == '__main__':
    c = Coffe()
    c.play()
