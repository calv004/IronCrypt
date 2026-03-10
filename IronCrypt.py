import sys
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

if len(sys.argv) != 3:
    print("You didnt provide enough arguments")
    exit()

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

    if sys.argv[2] == "encrypt":
        key = get_random_bytes(32)
        write_file("key.txt", key)

        bytes_text = read_file(sys.argv[1])

        nonce, tag, ciphertext = encrypt(bytes_text, key)
        write_file("nonce.txt", nonce)
        write_file("tag.txt", tag)

        write_file(sys.argv[1], ciphertext)

        print("File got encrypted")

    elif sys.argv[2] == "decrypt":

        decrypted_output = decrypt(read_file(sys.argv[1]), read_file("key.txt"), read_file("nonce.txt"), read_file("tag.txt"))
        write_file(sys.argv[1], decrypted_output)
        print("File decrypted successfully")

    else:
        print("You didnt provide the right arguments")