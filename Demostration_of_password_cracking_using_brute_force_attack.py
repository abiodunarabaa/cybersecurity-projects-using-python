import itertools
import string
import hashlib

# Function to hash a password using SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to generate all possible passwords of a given length from a given character set
def generate_passwords(length, charset):
    return (''.join(candidate) for candidate in itertools.product(charset, repeat=length))

# Function to perform a brute force attack
def brute_force_attack(target_hash, max_length, charset):
    for length in range(1, max_length + 1):
        for password in generate_passwords(length, charset):
            hashed_password = hash_password(password)
            if hashed_password == target_hash:
                return password
    return None

# Example usage
if __name__ == "__main__":
    target_hash = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"  # SHA-256 hash of the password "password"
    max_length = 8  # Maximum length of the password
    charset = string.ascii_lowercase + string.ascii_uppercase + string.digits  # Character set to use (lowercase, uppercase, and digits)
    
    cracked_password = brute_force_attack(target_hash, max_length, charset)
    if cracked_password:
        print(f"Password cracked: {cracked_password}")
    else:
        print("Password not found")
        
        
 
 
#This script first defines a function hash_password to hash a given password using the SHA-256 algorithm. 
#Then, it defines a function generate_passwords to generate all possible passwords of a given length from
# a given character set. Finally, it defines the brute_force_attack function to perform the actual brute 
#force attack by iterating through all possible password combinations until a match is found.