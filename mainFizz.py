# Fizz Buzz Problem
# Written by Spencer Villarreal

# 1) Count 1, 2, 3, 4, 5 . . .
# 2) When there are multiples of 3 print "Fizz" instead
# 3) Where there are multiples of 5 print "Buzz" instead
# 4) When there is a multiple of both (i.e) 15, print "FizzBuzz" instead
import os, time

os.system("clear")

uPick = input("How many times should Fizz Buzz run? => ")
pSpeed = input("Print Speed (Fast = 0.1  Slow = 1) => ")

try:
	value = int(uPick)
	speedValue = float(pSpeed)

	i = 1
	fizzCount = 0
	buzzCount = 0
	fizzbuzzCount = 0

	while i < value + 1:


		if i%15 == 0:
				fizzbuzzCount += 1
				print("Fizz Buzz   <=======")
				print("-----------")
		else:

			if(i%3 == 0 or i%5 == 0):

				if i%3 == 0:
					fizzCount += 1
					print("Fizz")
					print("-----------")
				if i%5 == 0:
					buzzCount += 1
					print("Buzz")
					print("-----------")
			
			elif(i%3 != 0 and i%5 != 0):
				print(i)
				print("-----------")

		i += 1
		time.sleep(speedValue)

	print("")
	print("--------------------")
	print("Fizz Count: " + str(fizzCount))
	print("--------------------")
	print("Buzz Count: " + str(buzzCount))
	print("--------------------")
	print("Fizz Buzz Count: " + str(fizzbuzzCount))
	print("--------------------")
	print("")
except ValueError:
	os.system("clear")
	print("!@!@!@!@!@!@!@!@!@!@!@!@!@!@!")
	print("Error: Please enter a number")
	time.sleep(1.5)
	os.system("python mainFizz.py")
