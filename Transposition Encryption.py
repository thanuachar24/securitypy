import math

# Encryption method which takes in the message and the key
def encryptMessageWithoutKey(msg, size):
	
	#Blank string to store the encrypted text
	cipher = ""
	
	# track key indices
	k_indx = 0

	#Length of the key to find the size of the columns
	msg_len = float(len(msg))
	
	#converting the message into lists for handling 
	msg_lst = list(msg)
	
	#sorting the list of keys to identify the order of transposition
	key_lst = [item for item in range(0, size)]
	# calculate column of the matrix
	col = size
	#can take user input for the number of columns if key is not required

	# calculate maximum row of the matrix
	row = int(math.ceil(msg_len / col))

	# add the padding character '_' in the empty cell of the matrix
	fill_null = int((row * col) - msg_len)
	msg_lst.extend('_' * fill_null)

	# create Matrix and insert message and padding characters row-wise
	matrix = [msg_lst[i: i + col] for i in range(0, len(msg_lst), col)]

	# read matrix column-wise using key
	for _ in range(col):
		#current index
		curr_idx = key_lst.index(k_indx)
		#adding the required alphabet from the matrix into the string called cipher
		cipher += ''.join([row[curr_idx] for row in matrix])
		#incrementing the index
		k_indx += 1
		#end for

	#print(cipher)
	return cipher

def encryptMessagewithKey(msg, key):
	#Blank string to store the encrypted text
	cipher = ""
	
	# track key indices
	k_indx = 0

	#Length of the key to find the size of the columns
	msg_len = float(len(msg))
	
	#converting the message into lists for handling 
	msg_lst = list(msg)
	
	#sorting the list of keys to identify the order of transposition
	key_lst = sorted(list(key))

	# calculate column of the matrix
	col = len(key)
	#can take user input for the number of columns if key is not required

	# calculate maximum row of the matrix
	row = int(math.ceil(msg_len / col))

	# add the padding character '_' in the empty cell of the matrix
	fill_null = int((row * col) - msg_len)
	msg_lst.extend('_' * fill_null)

	# create Matrix and insert message and padding characters row-wise
	matrix = [msg_lst[i: i + col] for i in range(0, len(msg_lst), col)]

	# read matrix column-wise using key
	for _ in range(col):
		#current index
		curr_idx = key.index(key_lst[k_indx])
		#adding the required alphabet from the matrix into the string called cipher
		cipher += ''.join([row[curr_idx] for row in matrix])
		#incrementing the index
		k_indx += 1
		#end for

	#print(cipher)
	return cipher

def transpositionWithoutKey():
	#First transposition of the message
	cipher = encryptMessageWithoutKey(msg, size)

	#Displaying the intermediate stage
	print(f"\nTranspotion Cipher of message '{msg}' with key size '{size}':\t", cipher)

def doubleTranspositionwithoutKey():
	#First transposition of the message
	stage_1 = encryptMessageWithoutKey(msg, size)

	#Displaying the intermediate stage
	print(f"\nSingle Transpotion Cipher of message '{msg}' with size '{size}':\t", stage_1)

	#Second transposition of the message i.e transposition of the cipher of stage 1
	cipher = encryptMessageWithoutKey(stage_1, size)

	#Printing the final cipher text
	print(f"\nDouble transposed message '{msg}' with size '{size}' is\n\t'",cipher,"'")


def transpositionWithKey():
	#First transposition of the message
	cipher = encryptMessagewithKey(msg, key)

	#Displaying the intermediate stage
	print(f"\nTranspotion Cipher of message '{msg}' with key '{key}':\t", cipher)




def doubleTransposition():
	#First transposition of the message
	stage_1 = encryptMessagewithKey(msg, key)

	#Displaying the intermediate stage
	print(f"\nSingle Transpotion Cipher of message '{msg}' with key '{key}':\t", stage_1)

	#Second transposition of the message i.e transposition of the cipher of stage 1
	cipher = encryptMessagewithKey(stage_1, key)

	#Printing the final cipher text
	print(f"\nDouble transposed message '{msg}' with key '{key}' is\n\t'",cipher,"'")




main_choice = int(input ("Enter 1 for encryption without key\nEnter 2 for encryption with key\t"))
if (main_choice == 1):
	choice = int(input("_____\nEnter 1 for transposition\nEnter 2 for Double transposition\t"))
	msg = input ("_____\nEnter the message to be encrypted: ")
	size = int(input ("Enter the column: "))

	if (choice == 1):
		transpositionWithoutKey()
	elif (choice == 2):
		doubleTranspositionwithoutKey()
	else:
		print("Terminated for a wrong input")

elif(main_choice ==2):
	choice = int(input("_____\nEnter 1 for transposition with key\nEnter 2 for Double transposition with key\t"))
	msg = input ("_____\nEnter the message to be encrypted: ")
	key = input ("Enter the key for encryption: ")

	if (choice == 1):
		transpositionWithKey()
	elif (choice == 2):
		doubleTransposition()
	else:
		print("Terminated for a wrong input")
else:
	print("Terminated for a wrong input")
