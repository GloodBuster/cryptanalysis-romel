def monoalphabetic_cipher(text, key):
    from utils import clean_text, generate_substitution_dictionary
    text = clean_text(text)
    key = clean_text(key)
    
    substitution_dictionary = generate_substitution_dictionary(key)
    
    cipher_text = ""
    for char in text:
        if char in substitution_dictionary:
            cipher_text += substitution_dictionary[char]
        else:
            cipher_text += char

    return cipher_text
