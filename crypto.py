import re, secrets, sys

# XOR with repeating key
def xor_repeating(data: bytes, key: bytes) -> bytes:
    return bytes(a ^ b for a, b in zip(data, key * (len(data) // len(key) + 1)))

# convert hex string to bytes
def hex_to_bytes(hex: str, argument: str) -> bytes:
    if argument == "Key" and not hex:
        print("Error: Key is empty", file=sys.stderr)
        sys.exit(1)
    if len(hex) % 2 != 0:
        print(f"Error: { argument } has an odd number of hex digits", file=sys.stderr)
        sys.exit(1)
    if hex != hex.strip():
        print(f"Error: { argument } contains leading or trailing whitespace", file=sys.stderr)
        sys.exit(1)
    if not re.fullmatch(r"[0-9a-fA-F]*", hex):
        print(f"Error: { argument } is not valid hex", file=sys.stderr)
        sys.exit(1)
    return bytes.fromhex(hex)


# key generation
def keygen(length: int) -> str:
    if length <= 0:
        print("Error: Key length must be a positive integer", file=sys.stderr)
        sys.exit(1)
    return secrets.token_hex(length)

# decryption
def decrypt(ciphertext: str, key: str) -> str:
    bytes_key = hex_to_bytes(key, "Key")
    bytes_ciphertext = hex_to_bytes(ciphertext, "Ciphertext")
    bytes_text = xor_repeating(bytes_ciphertext, bytes_key)
    try:
        return bytes_text.decode("utf-8")
    except UnicodeDecodeError:
        print("Error: Decrypted ciphertext is not valid UTF-8", file=sys.stderr)
        sys.exit(1)

# encryption
def encrypt(text: str, key: str) -> str:
    bytes_key = hex_to_bytes(key, "Key")
    bytes_text = text.encode("utf-8")
    bytes_ciphertext = xor_repeating(bytes_text, bytes_key)
    return bytes_ciphertext.hex()
