"""
Program : Bisection search

@author : Zishan jawed
"""
x = int(input("Enter the sqaure of any number: "))
count = 0
epsilon = 0.01
low = 1
high = x
ans = (high + low)/2.0


while abs(ans ** 2 -x) >= epsilon:
	print("low : {}  high : {}".format(low , high))
	count += 1
	if ans**2 < x:
		low = ans
	else:
		high = ans
	ans = (high + low)/2.0


print("Thsi progarm take {} guesses to find the square root of {} is : {}".format(count , x, ans))