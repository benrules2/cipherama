class RotationCipher:  
    def __init__(self, rot = 13):
        self.original_alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
             "n","o","p","q","r","s","t","u","v","w","x","y","z"]
        self.cipher_alphabet =  self.original_alphabet[rot:]
        self.cipher_alphabet.extend(self.original_alphabet[0:rot])      
        
    def encrypt_message(self, message):
        encrypted = ""
        for letter in message:
            if self.original_alphabet.count(letter) > 0:
                index = self.original_alphabet.index(letter)
                encrypted += self.cipher_alphabet[index]
            else:
                 encrypted += letter   
        return encrypted

    def decrypt_message(self, message):
        decrypted = ""
        for letter in message:
            if self.original_alphabet.count(letter) > 0:
                index = self.cipher_alphabet.index(letter)
                decrypted += self.original_alphabet[index]
            else:
                decrypted += letter
        return decrypted

            