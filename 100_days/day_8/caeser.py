
from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)

def caesar():
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  end_text = ""
  if shift > 26:
    shift = shift % 26
  if direction == "decode":
    shift *= -1

  for char in text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift
      end_text += alphabet[new_position]
    else:
      end_text += char

  print(f"Here's the {direction}d result: {end_text}\n")
  restart = input("Type 'y' to continue. Type 'n' to exit.\n").lower()

  if restart == "y":
    caesar()
  else:
    print("Goodbye")