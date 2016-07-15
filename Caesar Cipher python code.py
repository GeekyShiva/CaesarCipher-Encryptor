 # Caesar Cipher
 #bruh! I am back again with another Encryptor/Decyrptor/brute option available
 # I have developed this one to better up the understanding of the Cryptography and experimenting Caesar Cipher
 # Its a moderately complex prgram and has a very special feature of brute force.

MAX_KEY_SIZE = 26 # Key can't be bigger than 26(alphabets asshole***)

def getMode():        #function1

    while True:

        print('Do you wish to encrypt or decrypt or brute b a message?')

        mode = input().lower()

        if mode in 'encrypt e decrypt d brute b'.split():


            return mode

        else:

            print('Enter either "encrypt" or "e" or "decrypt" or "d" or "brute" or "b" .')



def getMessage():    #function2

              print('Enter your message:')

              return input()



def getKey():    #function3

             key = 0

             while True:

              print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))

              key = int(input())

             if (key >= 1 and key <= MAX_KEY_SIZE):

                              return key



def getTranslatedMessage(mode, message, key):

            if mode[0] == 'd':

               key = -key

            translated = ''



            for symbol in message:
               if symbol.isalpha():

                     num = ord(symbol)
                     num += key



                     if symbol.isupper():

                         if num > ord('Z'):

                             num -= 26

                         elif num < ord('A'):

                             num += 26
                     elif symbol.islower():

                         if num > ord('z'):

                             num -= 26

                         elif num < ord('a'):

                             num += 26



                     translated += chr(num)

            else:

                      translated += symbol

            return translated

mode = getMode()

message = getMessage()

if mode[0] != 'b':

    key = getKey()



print('Your translated text is:')

if mode[0] != 'b':

    print(getTranslatedMessage(mode, message, key))

else:

    for key in range(1, MAX_KEY_SIZE + 1):

        print(key, getTranslatedMessage('decrypt', message, key))


        #Loved my work you bitch,right? XD XD XD
        # I will explain the brute logic and usage of isalpha in the readme. (read it you d**khead)