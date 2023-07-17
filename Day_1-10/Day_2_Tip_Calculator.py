def tip_calculator():
    print('Welcome to the tip calculator.')
    bill = float(input('What was the total bill?$ '))
    tip = int(input('What percentage tip would you like to give? 5, 10 or 15 '))
    peoples = int(input('How many people to split the bill? '))

    tip = float(f"1.{tip}")
    result = (bill * tip) / peoples
    result = round(result, 2)
    print(f"Each person should pay: ${result}")


if __name__ == '__main__':
    tip_calculator()
