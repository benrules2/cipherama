import sys
import argparse

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
             "n","o","p","q","r","s","t","u","v","w","x","y","z",
             " ",",", "!","?", ".", "'", "\n", ";",":", "’"]

class SubstitutionCipher:  
    def __init__(self, key, offset = 0):
        self.original_alphabet = alphabet
        self.key = key
        self.cipher_alphabet = []

        #add the key as the first letters to scramble cipher alphabet
        tmp_alphabet = self.original_alphabet.copy()

        for letter in key:
            if letter in tmp_alphabet:
                tmp_alphabet.remove(letter)
            if not letter in self.cipher_alphabet:
                self.cipher_alphabet.append(letter)
        self.cipher_alphabet.extend(tmp_alphabet)

    def encrypt_message(self, message):
        encrypted = ""
        for letter in message:
            index = self.original_alphabet.index(letter)
            encrypted += self.cipher_alphabet[index]
        return encrypted

    def decrypt_message(self, message):
        decrypted = ""
        for letter in message:
            index = self.cipher_alphabet.index(letter)
            decrypted += self.original_alphabet[index]
        return decrypted
