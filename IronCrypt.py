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

    print(ciphertext)
    return nonce, tag, ciphertext

def decrypt(text, key, nonce):
    cipher_dec = AES.new(key, AES.MODE_GCM, nonce=nonce)
    plaintext = cipher_dec.decrypt_and_verify(text, tag)

    print(plaintext.decode())


if __name__ == '__main__':
    key = get_random_bytes(32)

    mytext = sys.argv[1]
    bytes_text = mytext.encode()
    nonce, tag, ciphertext = encrypt(bytes_text, key)

    decrypt(ciphertext, key, nonce)