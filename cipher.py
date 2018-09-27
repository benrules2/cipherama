import sys
import argparse
import substitution 
import shift


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A tool for encrypting and decrypting messages.')
    parser.add_argument('--key', help='secret word for substitution encryption', default="pythonisthebest", type=str)
    parser.add_argument('--action', help='options: encrypt, decrypt', default="encrypt", type=str)
    parser.add_argument('--cipher', help='options: shift, substitution', default="shift")
    parser.add_argument('--N', help='Alphabet offset(rotation cipher only)', default=13, type=int)
    parser.add_argument('--text', help='Message to encrypt or decrypt', type=str, required=True)
    args = parser.parse_args()

    cipher = None
    if args.cipher == "shift":
        cipher = shift.ShiftCipher(rot=args.N)
    elif args.cipher == "substitution":
        cipher = substitution.SubstitutionCipher(key=args.key)
    else:
        print("Cipher invalid {}".format(args.cipher))
        exit

    if args.action == "encrypt":
        print("Encrytped message: {}".format(cipher.encrypt_message(args.text)))
    elif args.action == "decrypt":
        print("Decrytped message: {}".format(cipher.decrypt_message(args.text)))
            