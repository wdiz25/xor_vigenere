import secrets, sys

# XOR with repeating key
def xor_repeating(data: bytes, key: bytes) -> bytes:
    return bytes(a ^ b for a, b in zip(data, key * (len(data) // len(key) + 1)))

# key generation
def keygen(length: int) -> str:
    return secrets.token_hex(length)

# decryption
def decrypt(ciphertext: str, key: str) -> str:
    bytes_key = bytes.fromhex(key)
    bytes_ciphertext = bytes.fromhex(ciphertext)
    bytes_text = xor_repeating(bytes_ciphertext, bytes_key)
    try:
        return bytes_text.decode("utf-8")
    except UnicodeDecodeError:
        print("Error: Decrypted ciphertext is not valid UTF-8", file=sys.stderr)
        sys.exit(1)

# encryption
def encrypt(text: str, key: str) -> str:
    bytes_key = bytes.fromhex(key)
    bytes_text = text.encode("utf-8")
    bytes_ciphertext = xor_repeating(bytes_text, bytes_key)
    return bytes_ciphertext.hex()
