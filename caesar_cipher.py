# Use printable ASCII characters for Caesar shift. Not limiting to alpha characters
LAST_CHAR_CODE = ord('~') # 126

# shifts the ASCII/Unicode value of each character in a message by the given key
# keep characters in the printable range
def caesar_shift(message, key):
    return ''.join(chr((ord(ch) + key) % (LAST_CHAR_CODE + 1)) for ch in message)

# check if string is an integer
def is_int_str(string):
    if string.isnumeric():
        return True
    elif string[0] == '-':
        if string[1:].isnumeric():
            return True
    return False

# add up ASCII values of characters in string
def force_int_value(string):
    return sum([ord(ch) for ch in string])

# gets user input and converts key to integer or adds up character values if int not detected
def get_key(prompt = 'Enter key (integer value): '):
    key = 0
    key_str = input(prompt)
    if is_int_str(key_str):
        key = int(key_str)
    else:
        key = force_int_value(key_str)
    return key

# Use the Caesar shift function to encrpyt, then decrypt a message with a given key
# Use key as-is to encrypt
# Negate key input to decrypt
def main():
    message = ''
    ciphertext = ''
    decrypted_message = ''
    key = 0

    print('Module 3: Assignment - Secure Hashing and Encryption')
    print('Caesar Cipher App')
    print('Enter a message and then a key.')

    message = input('\nEnter message: ')
    key = get_key()

    # encrypt message with key value
    ciphertext = caesar_shift(message, key)
    
    print('\nMessage encrypted!')
    print('Cipher text:', ciphertext)

    print('\nEnter the same key to decrypt the the ciphertext.')
    key = get_key()

    # negate key input to decrypt
    decrypted_message = caesar_shift(ciphertext, -key)
    
    print('\nMessage decrypted!')
    print('Message: ', decrypted_message)

# execute main function
if __name__ == '__main__':
    main()