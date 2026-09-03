import secrets

# Implement key generation
def keygen(length: int) -> str:
    return secrets.token_hex(length)

# Implement XOR with repeating key
def xor_repeating(data: bytes, key: bytes) -> bytes:
    return bytes(a ^ b for a, b in zip(data, key * (len(data) // len(key) + 1)))