#Encryption program

import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

key = chars.copy()
random.shuffle(key)

#ENCRYPT

plain_text = input("Enter what you want to ENCRYPT")
cipher_text = ""

for char in plain_text:
    index = chars.index(char)
    cipher_text += key[index]
    
#print(f"chars: {chars}")
#print(f"key: {key}")

print(f"plain_text: {plain_text}")
print(f"cipher_text: {cipher_text}")

#DECRYPT

cipher_text = input("Enter what you want to ENCRYPT")
plain_text = ""

for char in cipher_text:
    index = key.index(char)
    plain_text += chars[index]
    
print(f"cipher_text: {cipher_text}")
print(f"plain_text: {plain_text}")