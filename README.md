# cipherama
This is a repo for implementing ciphers from throughout history in python. 

It currently contains a shift cipher (aka Caesar's Cipher), and an alphabet
substitution cipher.

To run this, launch the cipher.py and provide the following arguments:

  -h, --help       show this help message and exit
  --key KEY        secret word for substitution encryption
  --action ACTION  options: encrypt, decrypt
  --cipher CIPHER  options: shift, substitution
  --N N            Alphabet offset(rotation cipher only)
  --text TEXT      Message to encrypt or decrypt


For example here is an encrypt / decrypt using the substitution cipher:

python3 cipher.py --cipher substitution --action encrypt --key "Greenday" --text "Hello World" 
Encrypted message: bdhhkzukohn

python3 cipher.py --cipher substitution --action decrypt --key "Greenday" --text "bdhhkzukohn" 
Decrypted message: hello world

And the same with shift cipher:

python3 cipher.py --cipher shift --action encrypt --text "Hello World" --N 7
Encrytped message: olssv dvysk

python3 cipher.py --cipher shift --action decrypt --text "olssv dvysk" --N 7
Decrytped message: hello world
