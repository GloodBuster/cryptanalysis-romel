from key_cipher import monoalphabetic_cipher
from decipher import monoalphabetic_decipher

text = "Buenas tardes, este es el mensaje mas secreto jamas creado en la historia de la humanidad."
key = "4$*P4Cjrk@XVBsopCBT!m9cT!,"

cipher_text = monoalphabetic_cipher(text, key)
print("Texto cifrado:", cipher_text)

decipher_text = monoalphabetic_decipher(cipher_text, key)
print("Texto descifrado:", decipher_text)
