from art import logo
print(logo)

# alphebet set is used twice so that for end alphabets like z, we can count shifting again from a
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        # if we want to decode the text then we need to substratct the position , so multiply by -1.
        shift_amount *= -1
    for char in start_text:
        # check if chracter is alphabet or special character
        if char.isalpha() == True:
            # for characters, shift the position as per direction
            position = alphabet.index(char)
            new_position = position + shift_amount
            # add shifed character in the string
            end_text += alphabet[new_position]
        else:
            # for special characters, don't shift the position, keep them as it is.
            end_text += char
    print(f"Here's the {cipher_direction} result: {end_text}")


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # To keep single shift if user enters shift > 26
    shift = shift % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    result = input(
        "Type Yes if you want to continue. Otherwise type No: ").lower()
    if result == "no":
        should_continue = False
        print("GoodBye")
