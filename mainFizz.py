# My Fizz Buzz Solution
# Written by Spencer Villarreal

# 1) Count 1, 2, 3, 4, 5 . . .
# 2) When there are multiples of 3 print "Fizz" instead
# 3) Where there are multiples of 5 print "Buzz" instead
# 4) When there is a multiple of both (i.e) 15, print "FizzBuzz" instead
import os, time

# Clear the system before running
os.system("clear")

# Ask for user variables
uPick = input("How many times should Fizz Buzz run? => ")
pSpeed = input("Print Speed (Fast = 0.1  Slow = 1) => ")

# Try and Run user variables with mainFizz
try:
	# Making sure user variables are int and float
	value = int(uPick)
	speedValue = float(pSpeed)

	# Variables for Fizz Buzz counter
	i = 1
	fizzCount = 0
	buzzCount = 0
	fizzbuzzCount = 0

	# While loop to print the count
	while i < value + 1:

		# If 'i' is a multiple of '15' print "Fizz Buzz"
		if i%15 == 0:
				fizzbuzzCount += 1
				print("Fizz Buzz   <=======")
				print("-----------")
		# If 'i' is not a multiple of '15' check for other multiples
		else:
			# If 'i' is a multiple of '3' or '5' print 'Fizz' or 'Buzz'
			if(i%3 == 0 or i%5 == 0):
				# 'i' is a multiple of '3'
				if i%3 == 0:
					fizzCount += 1
					print("Fizz")
					print("-----------")
				# 'i' is a multiple of '5'
				if i%5 == 0:
					buzzCount += 1
					print("Buzz")
					print("-----------")
			# If 'i' is nothing from above, then print the current number
			elif(i%3 != 0 and i%5 != 0):
				print(i)
				print("-----------")

		# Increase 'i' by 1 after every run
		i += 1
		# Adds a little delay for user to see whats going on
		time.sleep(speedValue)

	# Finished counting and here are the final results
	print("")
	print("--------------------")
	print("Fizz Count: " + str(fizzCount))
	print("--------------------")
	print("Buzz Count: " + str(buzzCount))
	print("--------------------")
	print("Fizz Buzz Count: " + str(fizzbuzzCount))
	print("--------------------")
	print("")
# The user did not enter a int or float into the user input
except ValueError:
	os.system("clear")
	print("!@!@!@!@!@!@!@!@!@!@!@!@!@!@!")
	print("Error: Please enter a number")
	time.sleep(1.5)
	os.system("python mainFizz.py")
