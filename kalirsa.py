#!/usr/bin/env python3

import rsa

# === Generate Kali key pair ===
(pubkey, privkey) = rsa.newkeys(2048)

# === Print the keys ===
print("Kali's Public Key:")
print(pubkey.save_pkcs1("PEM").decode("utf-8"))  # Print the public key
print("\nKali's Private Key:")
print(privkey.save_pkcs1("PEM").decode("utf-8"))  # Print the private key

# Save Kali's public key
with open("kalipublickey", "wb") as f:
    f.write(pubkey.save_pkcs1("PEM"))

# Save Kali's private key
with open("kaliprivatekey", "wb") as f:
    f.write(privkey.save_pkcs1("PEM"))


with open("kalipublickey", "rb") as f:
    public_key_content = f.read()
    print("Kali's Public Key File Content:")
    print(public_key_content.decode("utf-8"))  # Print the public key content

with open("kaliprivatekey", "rb") as f:
    private_key_content = f.read()
    print("\nKali's Private Key File Content:")
    print(private_key_content.decode("utf-8")) 




# === Load encrypted message ===
with open("encrypted_msg", "rb") as f:
    encrypted_message = f.read()

# Load Kali's private key
with open("kaliprivatekey", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())

# === Decrypt the message ===
try:
    decrypted_message = rsa.decrypt(encrypted_message, private_key)
    print("Decrypted message:", decrypted_message.decode())
except Exception as e:
    print("Decryption failed:", e)


