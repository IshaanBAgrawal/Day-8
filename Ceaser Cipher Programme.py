alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(message, shift_amount):
  global direction
  global alphabet
  if shift_amount > 26:
    shift_amount %= 26
  if direction == 'encode' or direction == 'encrypt':
    encoded_letters = ""
    for encoded_char in message:
      if encoded_char in alphabet:
        index_of_alphabet = alphabet.index(encoded_char)
        encoded_letters += alphabet[index_of_alphabet + shift_amount]
      else:
        encoded_letters += encoded_char
    print(f"The encrypted message is: {encoded_letters}.")
  elif direction == 'decode' or direction == 'decrypt':
    decoded_letters = ""
    for decoded_char in message:
      if decoded_char in alphabet:
        index_of_alphabet = alphabet.index(decoded_char)
        decoded_letters = decoded_letters + alphabet[index_of_alphabet - shift_amount]
      else:
        decoded_letters += decoded_char
    print(f"The decrypted message is: {decoded_letters}.")

from art import logo
print(logo)

choice_of_rerunning_the_program = 'y'

while choice_of_rerunning_the_program == "y":

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  caesar(message = text, shift_amount = shift)

  choice_of_rerunning_the_program = input("Do you want to rerun the program? Type 'y' for yes and 'n' for no.").lower()

print("Thanks for using our Ceaser Cipher programme.\n \n")
