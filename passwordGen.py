# 50 Projects Project Number 02
# Password generator that outputs a random string of symbols of specified length.

import sys, random

# Checks if CLA is valid:
if len(sys.argv) > 2:
	print("Please only enter one number.")
	quit()
elif not sys.argv[1].isdigit():
	print("Please only enter a numerical value.")
	quit()

# Declares variables:
length = int(sys.argv[1])
password = ""

# Loops over size length, generating a random character each time:
for i in range(length):
	code = random.randrange(33, 126)
	char = chr(code)
	password += char

with open("passwords.txt", "a") as f:
	f.write(password)
	f.write("\n")

print("Your generated password has been added to \"passwords.txt\"")
