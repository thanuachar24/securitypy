def encrypt(text,s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result
 
text = input("Enter the text")
s = 3
print ("Text  : " + text)
enc=encrypt(text,s)
print ("Cipher: " + enc )

def decrypt(enc,s1):
    result = ""
    for i in range(len(enc)):
        char = enc[i]
        if (char.isupper()):
            result += chr((ord(char) + s1 - 65) % 26 + 65)
        else:
            result += chr((ord(char) + s1 - 97) % 26 + 97)
    return result
 

s1 = -3
dec=decrypt(enc,s1)
print ("Cipher: " + dec )