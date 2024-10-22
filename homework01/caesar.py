def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for i in range(len(plaintext)):
        char = plaintext[i]
        final = ''
        if char == ' ':
            ciphertext += ' '
        elif char in '.,':
            ciphertext += char
        elif char.isdigit():
            ciphertext += char
        elif char.isalpha():
            stay = ord(char) + shift
            if char.islower():
                if stay > ord('z'):
                    stay -= 26
            if char.isupper():
                if stay > ord('Z'):
                    stay -= 26
            final = chr(stay)
        ciphertext += final
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        final = ''
        if char == ' ':
            plaintext += ' '
        elif char in '.,':
            plaintext += char
        elif char.isdigit():
            plaintext += char
        elif char.isalpha():
            stay = ord(char) - shift
            if char.islower():
                if stay < ord('a'):
                    stay += 26
            if char.isupper():
                if stay < ord('A'):
                    stay += 26
            final = chr(stay)
        plaintext += final
    return plaintext
