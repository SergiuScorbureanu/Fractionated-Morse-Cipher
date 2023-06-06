# Fractionated Morse Cipher

def encrypt_fractionated_morse(key, plaintext):
    morse_code = {
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..'
    }

    alphabet = []
    key = key.upper()
    for caracter in key:
        if caracter not in alphabet:
            alphabet.append(caracter)

    english_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for alph_letter in english_alphabet:
        if alph_letter not in alphabet:
            alphabet.append(alph_letter)

    encryption_list = ['...', '..-', '..x','.-.','.--','.-x','.x.','.x-','.xx','-..','-.-','-.x','--.','---','--x','-x.','-x-','-xx','x..','x.-','x.x','x-.','x--','x-x','xx.','xx-']
    
    morse_words_array = []
    for word in plaintext.split():
        separate_letters = []
        for char in word.upper():
            if char in morse_code:
                separate_letters.append(morse_code[char])
        morse_word = 'x'.join(separate_letters)
        morse_words_array.append(morse_word)
    morse_plaintext = 'xx'.join(morse_words_array)
    print("Textul tradus in codul Morse:")
    print(morse_plaintext)

    if len(morse_plaintext) % 3 != 0:
        count = 3 - (len(morse_plaintext) % 3)
        morse_plaintext += 'x' * count

    encrypted_text = ""
    for x in range(0, len(morse_plaintext), 3):
        character = morse_plaintext[x:x+3]
        for y in range(len(encryption_list)):
            if character == encryption_list[y]:
                encrypted_text += alphabet[y]

    return encrypted_text


def decrypt_fractionated_morse(key, plaintext):
    morse_code = {
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..'
    }

    alphabet = []
    key = key.upper()
    for caracter in key:
        if caracter not in alphabet:
            alphabet.append(caracter)

    english_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for alph_letter in english_alphabet:
        if alph_letter not in alphabet:
            alphabet.append(alph_letter)

    encryption_list = ['...', '..-', '..x','.-.','.--','.-x','.x.','.x-','.xx','-..','-.-','-.x','--.','---','--x','-x.','-x-','-xx','x..','x.-','x.x','x-.','x--','x-x','xx.','xx-']

    ecrypted_text = ""
    plaintext = plaintext.upper()

    for char in plaintext:
        if char in alphabet:
            index = alphabet.index(char)
            ecrypted_text += encryption_list[index]

    separate_words = ecrypted_text.split("xx")
    decrypted_text = ""
    for word in separate_words:
        separate_letters = word.split("x")
        for code in separate_letters:
            if code in morse_code.values():
                letter = list(morse_code.keys())[list(morse_code.values()).index(code)]
                decrypted_text += letter
            else:
                decrypted_text += " "
        decrypted_text += " "

    return decrypted_text.strip()



user_input = input("Introduceti 1 pentru criptarea unui mesaj sau 2 pentru decriptarea unui mesaj: ")

if user_input == "1":
    key = input("Introduceti cheia de criptare: ")
    plaintext = input("Introduceti textul pentru criptare: ")
    raw_text = encrypt_fractionated_morse(key, plaintext)
    ciphertext = ""
    for x in range(0, len(raw_text), 5):
        ciphertext += raw_text[x:x+5] + " "

    print("Textul encriptat:")
    print(ciphertext)

elif user_input == "2":
    key = input("Introduceti cheia de criptare: ")
    plaintext = input("Introduceti textul pentru decriptare: ")
    decrypted_text = decrypt_fractionated_morse(key, plaintext)
    print("Textul decriptat:")
    print(decrypted_text)

else:
    print("Optiunea introdusa nu este valida.")

