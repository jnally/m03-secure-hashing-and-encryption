# Module 3: Assignment - Secure Hashing and Encryption
**Author:** Jeremy Nally  
**Course:** SDEV245 - Security and Secure Coding  

## Overview & Cryptography Concepts
1. **Substitution Cipher (Caeser Cipher App):** A Python script that encrypts and decrypts text by shifting printable ASCII characters (I decided to use all of the printable ASCII characters instead of just letters). It relies on symmetric encryption. This means that the exact same key is used to both encrypt and decrypt the message.
2. **SHA-256 Hashing (Generate SHA-256 App):** A Python app using `hashlib` to generate fixed 256-bit hashes for strings and files. Hashing is irreversible and ensures data integrity since a one-character change alters the entire output.
3. **Digital Signatures using OpenSSL:** An OpenSSL simulation using an RSA 2048-bit key pair. The private key generates the signature, and the public key verifies it. This guarantees both the file's integrity and the sender's identity.

## How to Run the Code
* **Caesar Cipher App:** Run `python caesar_cipher.py` in the terminal and follow the prompts to enter your message and key.
* **Generate SHA-256 App:** Run `python sha256_hashing.py` in the terminal and choose the menu option to hash either text or a file.
* **Digital Signatures (OpenSSL on command line):** Please refer to the included screenshot for the `Verified OK` terminal output, demonstrating the `genrsa`, `rsa`, `dgst -sign`, and `dgst -verify` commands. See bash commands below:

```bash
echo "This is my secret." > secret.txt
openssl genrsa -out privkey.pem 2048
openssl rsa -in privkey.pem -pubout -out pubkey.pem
openssl dgst -sha256 -sign privkey.pem -out sign.sha256 secret.txt
openssl dgst -sha256 -verify pubkey.pem -signature sign.sha256 secret.txt

