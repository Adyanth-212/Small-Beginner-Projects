import random
import re

# Function to generate random characters
def generate_random_characters(count, start, end):
    return [chr(random.randrange(start, end)) for _ in range(count)]

# Define the regex pattern for a strong password
pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=]).{10,}$"

# Function to validate the password
def validate_password(password):
    if re.match(pattern, password):
        return True
    else:
        return False

# Main loop to generate a strong password
while True:
    # Get user input for allowed characters
    allowed_characters = input('What kinds of characters are allowed? (special, and lowercase, and uppercase, and numbers) ').split()

    # Initialize counts
    nospecialchr = nolowercase = nouppercase = nonumbers = 0

    # Get counts based on allowed characters
    if 'special' in allowed_characters:
        nospecialchr = int(input('How many special characters would you like? '))
    if 'lowercase' in allowed_characters:
        nolowercase = int(input('How many lowercase characters? '))
    if 'uppercase' in allowed_characters:
        nouppercase = int(input('How many uppercase characters? '))
    if 'numbers' in allowed_characters:
        nonumbers = int(input('How many numbers? '))

    # Generate random characters
    random_specialchr = generate_random_characters(nospecialchr, 33, 48) + generate_random_characters(nospecialchr, 58, 65)
    random_lowercase = generate_random_characters(nolowercase, 97, 123)
    random_uppercase = generate_random_characters(nouppercase, 65, 91)
    random_numbers = generate_random_characters(nonumbers, 48, 58)

    # Combine all characters
    password_characters = random_specialchr + random_lowercase + random_uppercase + random_numbers

    # Shuffle the characters to ensure randomness
    random.shuffle(password_characters)

    # Convert list to string
    password = ''.join(password_characters)

    # Validate the password
    if validate_password(password):
        print("Your password is:", password)
        print("It is a strong password.")
        break  # Exit the loop if the password is strong
    else:
        print("Generated password is not strong enough, generating a new one...")
