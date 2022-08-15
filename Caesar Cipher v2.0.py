from operator import index

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt (text = text, shift = shift):
    #Covert the text input into a list
    text_list = list(text)
    # print(text_list)

    #Initialize an empty string
    encoded_word = ""

    #Pick an element\ letter of the entered word from the generated list
    for elem in text_list:
        # print("")
        # print(elem)
        
        #Pick a letter from the list of alphabets
        for letter in alphabet:
            # print("The current alphabet being compared is "+letter)

            #Check whether the two match match
            if elem == letter:
                #Generate new index using shift
                encoded_index = alphabet.index(elem) + shift
                # print(encoded_index)

                #Condition where letter has been shifted outside the alhpabets
                if encoded_index > len(alphabet) -1:
                    encoded_index -= len(alphabet)
                    # print(f"New encoded index is {encoded_index}")

                encoded_letter = alphabet[encoded_index]
                # print("New letter is " +encoded_letter)

                #This also works
                # encoded_index1 = alphabet.index(letter) + shift
                # +encoded_letter1 = alphabet[encoded_index1]
                # print("New letter1 is " +encoded_letter1)

        #Concatinate the new letters into a new list
        encoded_word += encoded_letter
        # print(encoded_word)
    print("The encoded text is " +encoded_word)

def decrypt(text = text, shift = shift):
    #Initialize empty list
    decoded_word = ""
    text_list = list(text)
    for elem in text_list:
        for letter in alphabet:
            if elem == letter:
                decoded_index = alphabet.index(elem) - shift
                if decoded_index < 0:
                    decoded_index += len(alphabet)
                decoded_letter = alphabet[decoded_index]
            
        decoded_word += decoded_letter
    print("The decoded text is " +decoded_word)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
if direction == "encode":
    encrypt(text, shift)

elif direction == "decode":
    decrypt(text, shift)

else:
    print("You've entered the wrong choice")