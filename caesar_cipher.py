

FIRST_CHAR_CODE = ord(' ')
LAST_CHAR_CODE = ord('~')
CHAR_RANGE = LAST_CHAR_CODE - FIRST_CHAR_CODE

# shifts the ASCII/Unicode value of each character in a message by the given key
def caesar_shift(message, key): 
    print('first: ', FIRST_CHAR_CODE, ' last: ',LAST_CHAR_CODE, ' range: ', CHAR_RANGE)
    shifted_message = ''
    for ch in message:
        new_ch = (ord(ch) + key) % LAST_CHAR_CODE
        #new_ch = ord(ch) + key
        #if new_ch > LAST_CHAR_CODE:
        #    new_ch -= CHAR_RANGE
        #elif new_ch < FIRST_CHAR_CODE:
        #    new_ch += CHAR_RANGE
        print('ch: ',ch,ord(ch),' new_ch: ',chr(new_ch),new_ch)
        shifted_message += chr(new_ch)
    return shifted_message

# Use the Caesar shift function to encrpyt, then decrypt a message with a given key
def main():
    message = input('Enter message: ')
    key = int(input('Enter key: '))
    ciphertext = caesar_shift(message, key)
    print('Cipher text:', ciphertext)

    key = int(input('Enter key: '))
    print(caesar_shift(ciphertext, -key))
    return

# execute main function
if __name__ == '__main__':
    main()