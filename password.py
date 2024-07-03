import string
import random

def generate_password(length, character_set):
    characters = ''
    if '1' in character_set:
        characters += string.ascii_letters
    if '2' in character_set:
        characters += string.digits
    if '3' in character_set:
        characters += string.punctuation
    return ''.join(random.choices(characters, k=length))

print("Choose character set for password from these: ")
print("1. Digits")
print("2. Letters")
print("3. Special characters")
print("4. Exit")

length = None
while True:
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("Length must be a positive integer.")
        else:
            break
    except ValueError:
        print("Invalid input! Please enter a valid number.")

character_set_input = input("Enter numbers for the character sets you want to include (comma-separated, e.g., '1,2,3'): ")
character_set = character_set_input.split(',')

while not set(character_set).issubset({'1', '2', '3', '4'}):
    print("Invalid input! Please pick from 1, 2, 3, 4.")
    character_set_input = input("Enter numbers for the character sets you want to include (comma-separated, e.g., '1,2,3'): ")
    character_set = character_set_input.split(',')

password = generate_password(length, character_set)

print("The random password is:", password)