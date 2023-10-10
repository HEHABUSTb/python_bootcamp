alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


finish = False

while finish is False:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    def ceaser(direction: str, text: str, shift: int):
        output = ''

        # Check if shift number greater 25
        if shift % 25 > 0:
            while shift > 25:
                shift -= 25

        # If decode method multiple on -1
        if direction == 'encode':
            pass
        elif direction == 'decode':
            shift *= -1
        else:
            return print(f"Unexpected command {direction} enter 'decode' or 'encode'")

        # Create input
        for letter in text:
            if letter in alphabet:
                index = alphabet.index(letter)
                index += shift

                if direction == 'encode' and index > 25:
                    while index > 25:
                        index -= 26

                output += alphabet[index]
            else:
                output += letter

        print(f"The {direction}d text is {output}")

    ceaser(direction, text, shift)

    should_continue = input("Do you wanna continue? Type 'yes' or 'no':\n").lower()
    if should_continue == 'no':
        finish = True
        print('Terminated')




