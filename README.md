# Assignment 1: Repeating-Key XOR
### Author: William Disman

**Programming Language:** Python 3.12.14

**Program Dependencies:** None

**Test Dependencies:** pytest

## How to Run the Program
Users must have Python installed on their device. For users utilizing wasp.cs.kent.edu or hornet.cs.kent.edu, Python is already installed. For other devices, see official installation methods at [Python Setup and Usage](https://docs.python.org/3.12/using/index.html).

### Generating a Key
Users can use the `keygen` command to generate a random hexadecimal key to use for encryption. The length of the key should be a positive integer.
```text
python3 xor_vigenere.py keygen --length <positive integer>
```

### Encrypting Text
To encrypt text, users must have previously generated an encryption key. The `encrypt` command accepts a hexadecimal key and a UTF-8 string.
```text
python3 xor_vigenere.py encrypt --key <hex> --text <UTF-8 string>
```

### Decrypting Text
To decrypt text, users must have a ciphertext and associated key in hexadecimal format. The command to perform this action is `decrypt`.
```text
python3 xor_vigenere.py decrypt --key <hex> --ciphertext <hex>
```

## How to Test the Program
The automated test suite for this program is designed for pytest. Most users can run `pip3 install pytest` to install pytest in their Python environment. For more information about installing pytest, see [Get Started](https://docs.pytest.org/en/stable/getting-started.html).

To run the automated test suite, users should execute the `pytest` command inside this project's directory. Alternatively, users may execute the below command to explicitly test the provided tests.

```
pytest test_xor_vigenere.py
```

## Assumptions
The project was tested on Python 3.12.14. Depending on your operating system and environment setup, the `python` and `python3` commands may point to different versions of Python. To test what version of Python your system is running you can try the following commands.

```
python --version
python3 --version
```
Depending on your setup the `pip` and `pip3` commands may also point to different versions. For assistance with `pip`, see [Getting Started](https://pip.pypa.io/en/stable/getting-started/).

## References
The following sources were referenced throughout the course of the program's development. Github Copilot Inline Suggestions enabled by default in VS Code provided some assistance with repetitive lines of code such as xor_vigenere.py lines 10-22.

---

Argparse — Parser for Command-Line Options, Arguments and Subcommands — Python 3.14.7 Documentation. https://docs.python.org/3/library/argparse.html. Accessed 2 Sept. 2026.

Get Started - Pytest Documentation. https://docs.pytest.org/en/stable/getting-started.html. Accessed 4 Sept. 2026.
