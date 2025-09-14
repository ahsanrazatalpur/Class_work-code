def ceaser_decryption(cipher_text , key):
    result = ""
    for char in cipher_text:
        if char.isalpha():
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')
        char_position = ord(char) - base
        new_position = (char_position - key ) %26

        result+= chr(new_position + base)
    else:
        result+= char
        
        return result
    
ceaser_decryption("L oryh Sbwkrq!", 3) # "I love Python!"