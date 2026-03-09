# 🔐 AES File Encryptor

A lightweight command-line tool for encrypting and decrypting files using **AES-256-GCM** — one of the most secure symmetric encryption algorithms available.

---

## ✨ Features

- **AES-256-GCM** encryption (authenticated encryption with associated data)
- Random 256-bit key generation per session
- Integrity verification via GCM authentication tag
- In-place file encryption & decryption
- Minimal dependencies

---

## 📋 Requirements

- Python 3.x
- [pycryptodome](https://pycryptodome.readthedocs.io/)

Install the dependency:

```bash
pip install pycryptodome
```

---

## 🚀 Usage

```bash
python encryptor.py <file_path>
```

### Example

```bash
python encryptor.py secret.txt
```

1. The file is **encrypted in-place** using a freshly generated AES-256 key.
2. Press **Enter** to decrypt the file back to its original content.

> ⚠️ **Note:** The key is generated in-memory and not saved. Once the program exits, the key is lost and the file cannot be recovered. Do not close the program before decrypting.

---

## 🔒 How It Works

| Step | Description |
|------|-------------|
| 1 | A random 256-bit key is generated using a cryptographically secure RNG |
| 2 | A unique nonce is created for the AES-GCM cipher |
| 3 | The file is read as raw bytes and encrypted |
| 4 | The ciphertext is written back to the original file path |
| 5 | On user confirmation, the file is decrypted and verified via the GCM tag |

**AES-GCM** provides both confidentiality and authenticity — any tampering with the ciphertext will cause decryption to fail.

---

## 📁 Project Structure

```
.
└── encryptor.py    # Main encryption/decryption script
```

---

## ⚠️ Disclaimer

This tool is intended for **educational and personal use** only. The key is held in memory for the duration of the session and is not persisted anywhere. Use a proper key management solution for production scenarios.

---

