import secrets, tools

# Implement key generation
def keygen(length: int) -> str:
    return secrets.token_hex(length)

# Implement decryption
def decrypt(ciphertext: str, key: str) -> str:
    bytes_key = bytes.fromhex(key)
    bytes_ciphertext = bytes.fromhex(ciphertext)
    bytes_text = tools.xor_repeating(bytes_ciphertext, bytes_key)
    return bytes_text.decode("utf-8")

# Implement encryption
def encrypt(text: str, key: str) -> str:
    bytes_key = bytes.fromhex(key)
    bytes_text = text.encode("utf-8")
    bytes_ciphertext = tools.xor_repeating(bytes_text, bytes_key)
    return bytes_ciphertext.hex()