
import _Art
import alphanumeric

print(_Art.ceasar_cipher_logo)

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
# 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alphabet = alphanumeric.letters_lower

should_continue = "yes"
# final_text = ""

def ceasar_cipher(cipher_direction, start_text, shift_amount):
    final_text = ""

    if shift_amount >= 25:
        shift_amount %= 25

    if cipher_direction == "decode":
        shift_amount *= -1

    for char in start_text:
        if char not in alphanumeric.letters_lower:
            final_text += char
        else:
            new_index = alphabet.index(char) + shift_amount

            if new_index > 25:
                new_index %= 25
                new_index -= 1

            new_letter = alphabet[new_index]
            final_text += new_letter
    
    print("Your " +cipher_direction+ "d text is :" +final_text)
    print("")


while should_continue == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    ceasar_cipher(cipher_direction = direction, start_text= text, shift_amount= shift)

    should_continue = input("Type 'yes' to go again. Otherwise type 'no': ").lower()
    print("")
    print("")

print("Goodbye")