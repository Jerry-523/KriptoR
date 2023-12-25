import os
from cryptography.fernet import Fernet
import pyfiglet

banner = pyfiglet.figlet_format("KRYPTOR")
print(banner)
print("                            @Jerry-523\n\n")
print("  Select: \n")
print("----------------------------------------\n")
print("	Encrypt Files ---------->[1]\n")
print("	Decrypt Files ---------->[2]\n")
print("----------------------------------------")

x = int(input("\n	--> "))

if x == 1:
	
	files = []

	for file in os.listdir():
		if file == "kryptor.py" or file == "thekey.key":
		        continue
		if os.path.isfile(file):
		        files.append(file)
		        
	key = Fernet.generate_key()
	

	with open("thekey.key", "wb") as thekey:
		thekey.write(key)

	for file in files:
		with open(file, "rb") as thefile:
		        contents = thefile.read()
		contents_encrypted = Fernet(key).encrypt(contents)
		with open(file, "wb") as thefile:
		        thefile.write(contents_encrypted)
	print("\n  Done")

if x == 2:
	files = []

	for file in os.listdir():
		if file == "kryptor.py" or file == "thekey.key":
		        continue
		if os.path.isfile(file):
		        files.append(file)

	with open("thekey.key", "rb") as key:
		secretkey = key.read() 
		
	for file in files:
			with open(file, "rb") as thefile:
				contents = thefile.read()
			contents_decrypted = Fernet(secretkey).decrypt(contents)
			with open(file, "wb") as thefile:
				thefile.write(contents_decrypted)
	print("\n  Done")

		


