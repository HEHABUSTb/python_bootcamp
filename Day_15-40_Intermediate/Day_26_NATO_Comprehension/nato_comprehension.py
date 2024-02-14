import pandas

# Read csv and create data frame
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Loop through rows of a data frame old version
for (index, row) in data.iterrows():
    # Access index and row
    # Access row.student or row.score
    # print(row.letter)
    # print(row.code)
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
# TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
nato_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}
print(nato_alphabet)


def nato():
    try:
        # TODO 2. Create a list of the phonetic code words from a word that the user inputs.
        user_input = input(f"Enter your word: ")
        result = [nato_alphabet[letter] for letter in user_input.upper()]
        print(result)
    except KeyError as e:
        print('Sorry only letters please')
        nato()


nato()
