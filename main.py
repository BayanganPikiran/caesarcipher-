alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    caesar_message = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            caesar_message += alphabet[new_position]
        else:
            caesar_message += char
    print(f"Your {cipher_direction}d message is: {caesar_message}.")


should_continue = True

while should_continue:
    direction = input("Welcome to Caesar's Cipher.  Would you like to 'encode' or 'decode'?: \n").lower()
    shift = int(input("How many characters do you wish to shift your message by?: \n"))
    shift = shift % 26
    text = input("What message do you wish to cipher?: \n")

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    repeat = input("Do you have more messages to cipher? 'Yes' or 'No'?: \n").lower()
    if repeat == "no":
        should_continue = False
        print("Hail, Caesar!")