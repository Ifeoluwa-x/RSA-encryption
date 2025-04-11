#!/usr/bin/env python3

import rsa

# === Generate Ubuntu key pair ===
(pubkey, privkey) = rsa.newkeys(2048)

# Save Ubuntu's public key
with open("ubuntupublickey", "wb") as f:
    f.write(pubkey.save_pkcs1("PEM"))

# Save Ubuntu's private key
with open("ubuntuprivatekey", "wb") as f:
    f.write(privkey.save_pkcs1("PEM"))

# === Print the public and private keys ===
print("Public Key:")
print(pubkey.save_pkcs1("PEM").decode("utf-8"))  # Print the public key
print("\nPrivate Key:")
print(privkey.save_pkcs1("PEM").decode("utf-8"))  # Print the private key

# === Load Kali's public key ===
with open("kalipublickey", "rb") as f:
    kalipubkey = rsa.PublicKey.load_pkcs1(f.read())

# === Encrypt message using Kali's public key ===
print("Waiting for user input...")
message = input("Enter message to encrypt (min 15 chars): ").encode('utf-8')
if len(message) < 15:
    print("Message must be at least 15 characters!")
    exit()

# RSA can only encrypt limited size data
if len(message) > 200:
    print("Message too long for RSA (max ~200 chars)")
    exit()
encrypted_message = rsa.encrypt(message, kalipubkey)

# Save encrypted message
with open("encrypted_msg", "wb") as f:
    f.write(encrypted_message)

print("Message encrypted and saved as 'encrypted_msg'")
