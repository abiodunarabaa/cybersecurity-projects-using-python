import string
import secrets

def generate_random_password(length=12):
    # Define the character sets for different types of characters
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate a random password by selecting characters randomly
    password = ''.join(secrets.choice(all_characters) for _ in range(length))
    
    return password

# Example usage: generate a random password with default length of 12 characters
random_password = generate_random_password()
print("Random password:", random_password)
