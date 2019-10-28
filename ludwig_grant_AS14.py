# File Name: ludwig_grant_AS14.py
# File Path: /home/ludwigg/Python/PyRpi_AS14/ludwig_grant_AS14.py
# Run Command: sudo python3 /home/ludwigg/Python/PyRpi_AS14/ludwig_grant_AS14.py

# Grant Ludwig
# 10/28/2019
# AS.14
# Validate a number is a factor of something

import random

def isPrime(num):
	if num > 1:
		for i in range(2, num):
			if (num % i) == 0:
				return False
	return True

def getPrimeNumber():
	num = 1
	while (isPrime(num)):
		num = random.randrange(0,100)
	return num

play = True

while play:
	number = getPrimeNumber()
	factor = input("Enter a factor of " + str(number) + ": ")
	result = float(number / int(factor))
	if result.is_integer():
		print(factor, "is a factor of", number)
	else:
		print(factor, "is not a factor of", number)
	question = input("Play again? (Y/N) ")
	if question == "Y" or question == "y":
		play = True
	else:
		play = False