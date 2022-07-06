
import Encryption

#reading from file

plain_text = open("Plain Text.txt", "r+")

text = plain_text.read()

text = text.lower()
#print("Text: ", text)



#CAESAR CIPHER

def caesarCipher():

    #key size 
    s = 3
    #print ("Shift : " + str(s))

    Cipher = Encryption.Shift(text,s)

    #print("Cipher: ", Cipher)
    
    return Cipher 

#Shift Cipher with user defined key from 1 to 25 
def shiftCipher():

    #key size
    s = int (input("Enter the key size from 1 to 25."))

    Cipher = Encryption.Shift(text, s)

    #print("Cipher: ", Cipher)
    
    return Cipher


def rot13():
    #key size
    s = 13

    Cipher = Encryption.Shift(text, s)

    #print("Cipher: ", Cipher)
    
    return Cipher

#Vatsyayana Cipher dictionary
CIPHER_DICT = {'e': 'u', 'b': 's', 'k': 'x', 'u': 'q', 'y': 'c', 'm': 'w', 'o': 'y', 'g': 'f', 'a': 'm', 'x': 'j', 'l': 'n', 's': 'o', 'r': 'g', 'i': 'i', 'j': 'z', 'c': 'k', 'f': 'p', ' ': 'b', 'q': 'r', 'z': 'e', 'p': 'v', 'v': 'l', 'h': 'h', 'd': 'd', 'n': 'a', 't': ' ', 'w': 't'}

def vatsyayanaCipher():

    Cipher = Encryption.Vatsyayana(text, CIPHER_DICT)

    return Cipher

#Writing to file

cipher_text = open("Cipher Text.txt", "w")

cipher_text.write("Plain Text\n")

cipher_text.write(text)

cipher_text.write("\n\nCaesar Cipher\n")

cipher_text.write(caesarCipher())

cipher_text.write("\n\nShift Cipher Cipher\n")

cipher_text.write(shiftCipher())

cipher_text.write("\n\nROT-13 Cipher\n")

cipher_text.write(rot13())

cipher_text.write("\n\nVatsyayana Cipher\n")

cipher_text.write(vatsyayanaCipher())