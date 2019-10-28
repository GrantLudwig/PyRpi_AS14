import random

def isPrime(num):
	if num > 1:
		for i in range(2, num):
			if (num % i) == 0:
				return False
	return True

def getPrimeNumber():
	num = 1
	while (!isPrim(num))
		num = random.randRange(0,100)
	return num

play = True

while play:
	number = getPrimeNumber()
	factor = input("Enter a factor of ", str(number) + ": ")
	result = number / factor
	if type(result) == int:
		print(factor, "is not a factor of", number)
	else:
		print(factor, "is a factor of", number)
	question = input("Play again? (Y/N) ")
	if question == "Y" or question == "y"
		play = True
	else:
		play = False