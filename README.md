
# 🔐 RSA Encryption Lab – Scripting For Cybersecurity

![Python](https://img.shields.io/badge/python-3.12-blue.svg)
![RSA](https://img.shields.io/badge/crypto-RSA-brightgreen)
![OS](https://img.shields.io/badge/platform-Ubuntu%20%7C%20Kali-red)

> Lab assignment focused on **RSA asymmetric encryption** between two virtual machines (Ubuntu & Kali) using Python.  
> Completed for **CSIS 3560 – Cybersecurity Fundamentals** by `Ifeoluwa`.

---

## 📜 Overview

This lab demonstrates the fundamentals of **asymmetric encryption** using the RSA algorithm. Two virtual machines simulate secure communication:
- Each VM generates an RSA key pair.
- Public keys are exchanged securely.
- Ubuntu encrypts a message using Kali’s public key.
- Kali decrypts the message using its private key.

The lab emphasizes hands-on application of cryptographic principles, secure key exchange, and controlled session logging.

---

## 🧰 Technologies Used

- 🐍 Python 3.12
- 🔐 [`rsa`](https://stuvel.eu/python-rsa-doc/) cryptography library
- 🖥️ VirtualBox VMs (Ubuntu 22.04 LTS and Kali Rolling)
- 🧪 `script` command for timestamped terminal logging
- 🔄 `scp` (secure copy) for file transfers between VMs
- 🗃️ `tar.gz` compression for submission packaging

---

## 📂 Folder Structure

```
a1iar64/
├── kalilogiar64.txt          # Kali terminal session log
├── kalidecrypt.png           # Screenshot: Decryption result in Kali
├── kaliprivatekey            # Kali private RSA key (PEM)
├── kalipublickey             # Kali public RSA key (PEM)
├── kalirsa.py                # Decryption script on Kali
├── ubuntologiar64.txt        # Ubuntu terminal session log
├── ubunduencrypt.png         # Screenshot: Encryption result in Ubuntu
├── ubuntuprivatekey          # Ubuntu private RSA key (PEM)
├── ubuntupublickey           # Ubuntu public RSA key (PEM)
├── ubuntursa.py              # Encryption script on Ubuntu
```

---

## 🧪 Step-by-Step Workflow

### 🛠️ 1. Environment Setup

```bash
# Create and activate virtual environment
python3 -m venv rsa_env
source rsa_env/bin/activate

# Install RSA library
pip install rsa
```

---

### 🔐 2. RSA Key Generation

On both **Ubuntu** and **Kali**, a 2048-bit RSA key pair is generated for enhanced encryption capacity.

```python
(pubkey, privkey) = rsa.newkeys(2048)

with open("publickey", "wb") as f:
    f.write(pubkey.save_pkcs1("PEM"))
with open("privatekey", "wb") as f:
    f.write(privkey.save_pkcs1("PEM"))
```

---

### 🔄 3. Public Key Exchange

Kali's public key is securely transferred to Ubuntu using:

```bash
scp KaliPublicKey loggedIn_User@Ubuntu_ip:/home/preferred_location/publicKey.
```

---

### ✉️ 4. Encryption (Ubuntu)

- The message input is validated to be ≥15 characters.
- It is encoded to bytes and encrypted with Kali’s public key.
- The encrypted message is saved to a file for transfer.

```python
message = input("Enter message: ").encode()
encrypted = rsa.encrypt(message, kalipubkey)
with open("encrypted_msg", "wb") as f:
    f.write(encrypted)
```

📸 Screenshot saved as `ubunduencrypt.png`.

---

### 📤 5. Message Transfer

The encrypted message is transferred back to Kali:

```bash
scp encrypted_msg loggedIn_User@kali_ip:/home/preferred_location/publicKey.
```

---

### 🔓 6. Decryption (Kali)

- Kali loads the encrypted message and its private key.
- The message is decrypted and printed.

```python
with open("encrypted_msg", "rb") as f:
    encrypted = f.read()

decrypted = rsa.decrypt(encrypted, privkey)
print("Decrypted message:", decrypted.decode())
```

📸 Screenshot saved as `kalidecrypt.png`.

---

## 🧾 Session Logging

### Ubuntu
```bash
script -t 2> ubuntu.time -a ubuntologiar64.txt
```

### Kali
```bash
script -t 2> kali.time -a kalilogiar64.txt
```

This captures every command with timestamps for full transparency.

---

## ✅ Outcome

- Full RSA key generation and encryption/decryption lifecycle achieved.
- Secure message communication was simulated between VMs.
- Demonstrated real-world limitations and use-cases of public-key cryptography.

---

## 📚 Key Learnings

- RSA is limited in message size; 2048-bit keys allow for ~245 bytes of data.
- Public keys must be shared in binary format, not printed (ASCII) versions.
- Strings must be `.encode()`d into bytes before encryption.
- Proper cryptographic handling and logging are essential for secure workflows.

---

## 🔒 Security Best Practices

- Private keys were never transferred across systems.
- `scp` ensured secure key and message transfer.
- Messages and keys were stored in `PEM` format and handled in binary mode.

---

## 🚀 Future Improvements

- Implement hybrid encryption (RSA + AES) for longer and secure file encryption.
- Automate key exchange over secure sockets or API endpoints.
- Add exception handling and logging to improve robustness.

---

## 📸 Screenshots

- `ubunduencrypt.png` – Message encrypted on Ubuntu.
- `kalidecrypt.png` – Message decrypted on Kali.

---

## 📦 Submission Packaging

All deliverables were archived as:

```bash
tar -czvf rsa_encryption.tar.gz rsa_encryption/
```

As per instructions, the `.tar.gz` contains all required files and logs.

---

## 📜 License

This repository and its contents are part of coursework for CSIS 3560 and are not licensed for public or commercial reuse.

---

## 🤝 Acknowledgments

- [Python RSA Documentation](https://stuvel.eu/python-rsa-doc/)
- [Metech RSA Encryption Guide](https://medium.com/@metechsolutions/python-by-examples-rsa-encryption-decryption-d07a226430b4)

---
