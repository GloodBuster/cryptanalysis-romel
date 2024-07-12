import string

def clean_text(texto):
    allow_characters = set(string.ascii_letters + " " + "," + "." + "ñ" + "Ñ")
    clean_text = ''.join(char for char in texto if char in allow_characters)
    return clean_text

def complete_dictionary(dictionary):
    alphabet = string.ascii_letters + "ñ" + "Ñ"
    used_values = set(dictionary.values())
    
    for char in alphabet:
        if char not in dictionary:
            for potential_value in alphabet:
                if potential_value not in used_values:
                    dictionary[char] = potential_value
                    used_values.add(potential_value)
                    break
    return dictionary

def generate_substitution_dictionary(key):
    alphabet = string.ascii_letters + "ñ" + "Ñ"
    key = key.upper()
    
    # Eliminar duplicados de la clave
    key = ''.join(dict.fromkeys(key))
    
    # Crear el diccionario
    dictionary = {}
    key_index = 0
    for i in range(len(alphabet)):
        if key_index < len(key):
            dictionary[alphabet[i]] = key[key_index]
            key_index += 1
        
    dictionary = complete_dictionary(dictionary)
    return dictionary