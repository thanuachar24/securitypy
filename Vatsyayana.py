CIPHER_DICT = {'e': 'u', 'b': 's', 'k': 'x', 'u': 'q', 'y': 'c', 'm': 'w', 'o': 'y', 'g': 'f', 'a': 'm', 'x': 'j', 'l': 'n', 's': 'o', 'r': 'g', 'i': 'i', 'j': 'z', 'c': 'k', 'f': 'p', ' ': 'b', 'q': 'r', 'z': 'e', 'p': 'v', 'v': 'l', 'h': 'h', 'd': 'd', 'n': 'a', 't': ' ', 'w': 't'}
def Vatsyayana(text, CIPHER_DICT):
    textC = []
    for i in range(len(text)):
        textC = ''
        for i in text:
            textC = textC + str(CIPHER_DICT.get(i))
    return str(textC)

text=input("Enter the string: ")
vat=Vatsyayana(text, CIPHER_DICT)
print("ecrypted messege",vat)


def DecVatsyayana(vat, CIPHER_DICT):
    CDKlist = list(CIPHER_DICT.keys())
    CDVlist = list(CIPHER_DICT.values())
    for i in range(len(vat)):
        textP = ''
        for i in vat:
            index = CDVlist.index(i)
            textP = textP + str( CDKlist[index] )
    return str(textP)

print("Decrypted messege",DecVatsyayana(vat, CIPHER_DICT))


