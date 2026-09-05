import crypto
import re

def test_known_answers():
    plaintext = bytes.fromhex("41747461636b206174206461776e21")
    key = bytes.fromhex("494345")
    expected = bytes.fromhex("08373128202e6922316927243e2d64")
    result = crypto.xor_repeating(plaintext, key)
    assert result == expected

    plaintext = bytes.fromhex("68656c6c6f")
    key = bytes.fromhex("6b6579")
    expected = bytes.fromhex("030015070a")
    result = crypto.xor_repeating(plaintext, key)
    assert result == expected

    plaintext = bytes.fromhex("00010203feff")
    key = bytes.fromhex("a55a")
    expected = bytes.fromhex("a55ba7595ba5")
    result = crypto.xor_repeating(plaintext, key)
    assert result == expected

def test_encrypt_decrypt():
    plaintext = "Hello, World!"
    key = "d7b0c3cc"
    ciphertext = crypto.encrypt(plaintext, key)
    result = crypto.decrypt(ciphertext, key)
    assert result == plaintext

def test_empty_message():
    plaintext = ""
    key = "e4ffd4de"
    ciphertext = crypto.encrypt(plaintext, key)
    assert ciphertext == plaintext

def test_long_message():
    plaintext = "The quick brown fox jumps over the lazy dog"
    key = "471b5371"
    ciphertext = crypto.encrypt(plaintext, key)
    result = crypto.decrypt(ciphertext, key)
    assert result == plaintext

def test_long_key():
    plaintext = "Hi"
    key = "27081126f4fd3b60e0ccdc1a034b9d52"
    ciphertext = crypto.encrypt(plaintext, key)
    result = crypto.decrypt(ciphertext, key)
    assert result == plaintext

def test_multibyte_message():
    plaintext = "© 2026 William Disman 🖥️"
    key = "33d24902"
    ciphertext = crypto.encrypt(plaintext, key)
    result = crypto.decrypt(ciphertext, key)
    assert result == plaintext

def test_arbitrary_message():
    plaintext = bytes.fromhex("72036000e1fb6f9fbef19b0dd8c50c3e")
    key = bytes.fromhex('e8e5bbbade276762')
    expected = bytes.fromhex("9ae6dbba3fdc08fd561420b706e26b5c")
    result = crypto.xor_repeating(plaintext, key)
    assert result == expected

def test_invalid_inputs():
    # empty key
    try: 
        crypto.encrypt("Hello", "")
        assert False
    except SystemExit:
        pass
    # odd-length key
    try: 
        crypto.encrypt("World", "abc")
        assert False
    except SystemExit:
        pass
    # odd-length ciphertext
    try: 
        crypto.decrypt("abc", "5836b78f")
        assert False
    except SystemExit:
        pass
    # invalid key format
    try: 
        crypto.encrypt("Test", "xyz")
        assert False
    except SystemExit:
        pass
    # invalid ciphertext format
    try: 
        crypto.decrypt("xyz", "5836b78f")
        assert False
    except SystemExit:
        pass
    # key with whitespace
    try: 
        crypto.encrypt("Test", "    5836b78f")
        assert False
    except SystemExit:
        pass
    # ciphertext with whitespace
    try: 
        crypto.decrypt("c3169fdb    ", "5836b78f")
        assert False
    except SystemExit:
        pass
    # keygen with negative length
    try: 
        crypto.keygen(-3)
        assert False
    except SystemExit:
        pass
    # keygen with zero length
    try: 
        crypto.keygen(0)
        assert False
    except SystemExit:
        pass

def test_invalid_utf8():
    try: 
        crypto.decrypt("599195cf903097287f062a0672a25f30", "5836b78f")
        assert False
    except SystemExit:
        pass

def test_key_generation():
    key = crypto.keygen(16)
    assert len(key) == 32
    assert re.fullmatch(r"[0-9a-f]*", key)