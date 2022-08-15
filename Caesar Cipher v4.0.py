alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(cypher_direction, start_text, shift_amount):
    #Initialize empty string for the end text
    final_text = ""

    if cypher_direction == "decode":
            shift_amount *= -1

    for letter in start_text:
        
        new_index = alphabet.index(letter) + shift_amount
        new_letter = alphabet[new_index]
        final_text += new_letter

    print("The " +cypher_direction+"d text is: " +final_text)

caesar(cypher_direction = direction,start_text = text, shift_amount = shift)

