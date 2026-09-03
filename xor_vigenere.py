import argparse
import crypto

# Initialize argument parser
parser = argparse.ArgumentParser()

# Implement command selection
subparsers = parser.add_subparsers(dest="command", required=True)

# Implement keygen options
parser_keygen = subparsers.add_parser("keygen")
parser_keygen.add_argument("--length", type=int, required=True)

# Implement encrypt options
parser_encrypt = subparsers.add_parser("encrypt")
parser_encrypt.add_argument("--key", type=str, required=True)
parser_encrypt.add_argument("--text", type=str, required=True)

# Implement decrypt options
parser_decrypt = subparsers.add_parser("decrypt")
parser_decrypt.add_argument("--key", type=str, required=True)
parser_decrypt.add_argument("--ciphertext", type=str, required=True)

# Parse CLI arguments
args = parser.parse_args()
match args.command:
    case "keygen":
        print(crypto.keygen(args.length))
    case "encrypt":
        bytes_key = bytes.fromhex(args.key)
        bytes_text = args.text.encode("utf-8")
        bytes_ciphertext = crypto.xor_repeating(bytes_text, bytes_key)
        print(bytes_ciphertext.hex())
    case "decrypt":
        bytes_key = bytes.fromhex(args.key)
        bytes_ciphertext = bytes.fromhex(args.ciphertext)
        bytes_text = crypto.xor_repeating(bytes_ciphertext, bytes_key)
        print(bytes_text.decode("utf-8"))