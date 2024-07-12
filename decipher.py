def monoalphabetic_decipher(cipher_text, key):
    from utils import clean_text, generate_substitution_dictionary
    cipher_text = clean_text(cipher_text)
    key = clean_text(key)

    substitution_dictionary = generate_substitution_dictionary(key)

    substitution_dictionary = {v: k for k, v in substitution_dictionary.items()}
    original_text = ""
    for char in cipher_text:
        if char in substitution_dictionary:
            original_text += substitution_dictionary[char]
        else:
            original_text += char

    return original_text
