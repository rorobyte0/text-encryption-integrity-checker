import hashlib
import base64

# Caesar cipher: shifts letters A–Z and a–z by a given amount 
def caesar_shift(text: str, shift: int) -> str:
    result = []
    for ch in text:
        if 'a' <= ch <= 'z':
            result.append(chr((ord(ch) - ord('a') + shift) % 26 + ord('a')))
        elif 'A' <= ch <= 'Z':
            result.append(chr((ord(ch) - ord('A') + shift) % 26 + ord('A')))
        else:
            result.append(ch)  # keep characters unchanged
    return ''.join(result)

# XOR encryption on bytes, returned as Base64 for safe printing
def xor_encrypt(text: str, key: int) -> str:
    if not (0 <= key <= 255):
        raise ValueError("XOR key must be between 0 and 255")

     
    xored = bytes([ord(b) ^ key for b in text])
    return base64.b64encode(xored).decode("ascii")

# Reverse the XOR process to recover the origonal text
def xor_decrypt(encoded_text: str, key: int) -> str:
    raw = base64.b64decode(encoded_text) 
    original_bytes = bytes([b ^ key for b in raw])
    return ''.join([chr(b) for b in original_bytes])
    

# Generate SHA-256 hash
def sha256_hex(text: str) -> str:
    return hashlib.sha256(bytes([ord(c) for c in text])).hexdigest()

# User input
plaintext = input("Enter the message to encrypt (your name): ")
try:
    caesar_key = int(input("Enter Caesar shift key: "))
    xor_key = int(input("Enter XOR key: "))
except ValueError:
    print("Invalid input Keys must be numbers!")
    raise 

# Encryption steps
caesar_text = caesar_shift(plaintext, caesar_key)
cipher_xor = xor_encrypt(caesar_text, xor_key)
hash_value = sha256_hex(cipher_xor)

# Display results
print("\nEncrypted text :", cipher_xor)
print("SHA-256 hash:", hash_value)

# Decryption steps
xor_decrypt_text = xor_decrypt(cipher_xor, xor_key)
recovered_text = caesar_shift(xor_decrypt_text, -caesar_key)

print("\nRecovered plaintext:", recovered_text)

# check
#cipher_xor = cipher_xor + "1"   #  يغير الهاش
new_hash = sha256_hex(cipher_xor)

if new_hash == hash_value:
    print("check passed!! ciphertext is unchanged.")
else:
    print("check failed ciphertext has been altered!")
