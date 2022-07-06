def rot13(phrase):
   abc = "abcdefghijklmnopqrstuvwxyz"
   out_phrase = ""

   for char in phrase:
       out_phrase += abc[(abc.find(char)+13)%26]
   return out_phrase


phrase = input("Enter the string: ")

rot=rot13(phrase)

print("The encrypted messege :  " , rot)


def derot13(rot):
   abc = "abcdefghijklmnopqrstuvwxyz"
   out_phrase1 = ""

   for char in rot:
       out_phrase1 += abc[(abc.find(char)-13)%26]
   return out_phrase1

print("The decrypted messege: ", derot13(rot))