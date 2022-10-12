retry = "y"
while retry == "y":
	print ("what do you need?")
	print ("1")
	print ("2")
	print ("3")

	numer = input()
	if numer == "1":
		print("I love cock")	
	elif numer == "2":
		print("In my ass")	
	elif numer == "3":	
		print("Fart fart fart")
	else:
		print("no no no fuck off")
	retry = input("Play again? y/n")
	if retry == "y":
		continue
	if retry == "n":
		print ("Thank you for playing!")
	quit = input("Enter any key to terminate program")
	if quit == "":
		break