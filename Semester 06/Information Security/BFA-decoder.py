def ceaser_decryption(cipher_text, key):
    result = ""
    for char in cipher_text:
        if char.isalpha():     # is Alphabet a,b,c,.. opr A,B,C.. ?
            if char.isupper():  # is Uppercase A,B,C..
                base = ord('A') # then base will be 65 becasue Ascii of A is 65
            else:
                base = ord('a') # then base will be 97 becuase ascii code of a is 97
            
            char_position = ord(char) - base  # ord() built in fun give ascii of char  65-65=0
            new_position = (char_position - key) % 26 # %26 to get rid of -ve indexing 
            result += chr(new_position + base) 
        else:
            result += char
    return result

print(ceaser_decryption("Khoor Zruog!", 3))
ceaser_decryption("Khoor Zruog!", 3)
ceaser_decryption("L oryh Sbwkrq!", 3) # "I love Python!"
ceaser_decryption("Vhfuhw Phvvdjh!", 3) # "Secret Message!"



