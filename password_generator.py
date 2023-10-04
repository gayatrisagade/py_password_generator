#random password generator using python.

import random
import string

def generate_random_password(length):
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure the password is at least 8 characters long
    if length < 8:
        print("Password length should be at least 8 characters.")
        return None

    # Generate the random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Random Password Generator")
    while True:
        try:
            length = int(input("Enter the length of the password: "))
            password = generate_random_password(length)

            if password is not None:
                print("Generated Password:", password)
            
            another_password = input("Generate another password? (yes/no): ").lower()
            if another_password != "yes":
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()

