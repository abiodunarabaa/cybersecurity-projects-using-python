from cryptography.fernet import Fernet

# Generate a key for encryption and decryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_file(file_path):
    with open(file_path, 'rb') as file:
        plaintext = file.read()
    ciphertext = cipher_suite.encrypt(plaintext)
    with open(file_path + '.enc', 'wb') as file:
        file.write(ciphertext)

def decrypt_file(encrypted_file_path):
    with open(encrypted_file_path, 'rb') as file:
        ciphertext = file.read()
    plaintext = cipher_suite.decrypt(ciphertext)
    decrypted_file_path = encrypted_file_path[:-4]  # remove '.enc' extension
    with open(decrypted_file_path, 'wb') as file:
        file.write(plaintext)

# Example usage:
# Encrypt a file
encrypt_file('example.txt')
# Decrypt an encrypted file
decrypt_file('example.txt.enc')




#This script uses the Fernet symmetric encryption algorithm from the cryptography library to encrypt and decrypt files.
#The encrypt_file function reads the contents of a file, encrypts them, and writes the encrypted data to a new file with a .enc extension.
#The decrypt_file function reads the encrypted data from a file, decrypts it, 
#and writes the decrypted data to a new file with the .enc extension removed.