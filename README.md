# IronCrypt


🔐 AES File Encryptor
A lightweight command-line tool for encrypting and decrypting files using AES-256-GCM — one of the most secure symmetric encryption algorithms available.

✨ Features

AES-256-GCM encryption (authenticated encryption with associated data)
Random 256-bit key generation per session
Integrity verification via GCM authentication tag
In-place file encryption & decryption
Minimal dependencies


📋 Requirements

Python 3.x
pycryptodome

Install the dependency:
bashpip install pycryptodome

🚀 Usage
bashpython encryptor.py <file_path>
Example
bashpython encryptor.py secret.txt

The file is encrypted in-place using a freshly generated AES-256 key.
Press Enter to decrypt the file back to its original content.


⚠️ Note: The key is generated in-memory and not saved. Once the program exits, the key is lost and the file cannot be recovered. Do not close the program before decrypting.


🔒 How It Works
StepDescription1A random 256-bit key is generated using a cryptographically secure RNG2A unique nonce is created for the AES-GCM cipher3The file is read as raw bytes and encrypted4The ciphertext is written back to the original file path5On user confirmation, the file is decrypted and verified via the GCM tag
AES-GCM provides both confidentiality and authenticity — any tampering with the ciphertext will cause decryption to fail.

📁 Project Structure
.
└── encryptor.py    # Main encryption/decryption script

⚠️ Disclaimer
This tool is intended for educational and personal use only. The key is held in memory for the duration of the session and is not persisted anywhere. Use a proper key management solution for production scenarios.
