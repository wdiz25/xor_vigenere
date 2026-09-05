import argparse
import crypto

# initialize argument parser
parser = argparse.ArgumentParser()

# command selection
subparsers = parser.add_subparsers(dest="command", required=True)

# keygen options
parser_keygen = subparsers.add_parser("keygen")
parser_keygen.add_argument("--length", type=int, required=True)

# encrypt options
parser_encrypt = subparsers.add_parser("encrypt")
parser_encrypt.add_argument("--key", type=str, required=True)
parser_encrypt.add_argument("--text", type=str, required=True)

# decrypt options
parser_decrypt = subparsers.add_parser("decrypt")
parser_decrypt.add_argument("--key", type=str, required=True)
parser_decrypt.add_argument("--ciphertext", type=str, required=True)

# parse CLI arguments
args = parser.parse_args()
match args.command:
    case "keygen":
        print(crypto.keygen(args.length))
    case "encrypt":
        print(crypto.encrypt(args.text, args.key))
    case "decrypt":
        print(crypto.decrypt(args.ciphertext, args.key))
