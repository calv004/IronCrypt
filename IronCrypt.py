import sys
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

if len(sys.argv) != 2:
    print("You didnt provide enough arguments")
    exit()

key = get_random_bytes(32)

def encrypt(text, key):
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(text)

    nonce = cipher.nonce
    return nonce, tag, ciphertext

def decrypt(text, key, nonce, tag):
    cipher_dec = AES.new(key, AES.MODE_GCM, nonce=nonce)
    plaintext = cipher_dec.decrypt_and_verify(text, tag)
    return plaintext

def read_file(path):
    with open(path, "rb") as file:
        file_content = file.read()
    return file_content

def write_file(path, content):
    with open(path, "wb") as file:
        file.write(content)

if __name__ == '__main__':
    key = get_random_bytes(32)

    file_path = sys.argv[1]

    bytes_text = read_file(file_path)

    nonce, tag, ciphertext = encrypt(bytes_text, key)

    write_file(sys.argv[1], ciphertext)

    input("File got encrypted, press enter to decrypt")


    decrypted_output = decrypt(ciphertext, key, nonce, tag)
    write_file(sys.argv[1], decrypted_output)