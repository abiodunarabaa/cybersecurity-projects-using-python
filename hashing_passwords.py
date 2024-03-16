import hashlib

def hash_password(password):
    # Convert the password to bytes before hashing
    password_bytes = password.encode('utf-8')
    
    # Create a SHA-256 hash object
    hash_object = hashlib.sha256()
    
    # Update the hash object with the password bytes
    hash_object.update(password_bytes)
    
    # Get the hexadecimal representation of the hashed password
    hashed_password = hash_object.hexdigest()
    
    return hashed_password

# Example usage
password = "my_secure_password"
hashed_password = hash_password(password)
print("Hashed password:", hashed_password)
