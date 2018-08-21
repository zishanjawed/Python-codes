
print("Please think of a number between 0 and 100!")
low = 0
high = 100
c = "no"
ans = (high + low)/2.0
while  c != "c":
	print("Is your secret number {}?".format(int(ans)))
	print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
	c = input()
	if c == "l":
		low = ans
	elif c == "h":
		high = ans
	else:
		print("Game over. Your secret number was: {}".format(int(ans)))
		c = "c"
	ans = (high + low)/2.0
	ans = round(ans)
