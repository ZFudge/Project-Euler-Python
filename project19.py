# n! means n x (n − 1) x ... x 3 x 2 x 1
# For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!

def factorial(num):
	if num > 1:
		newNum = factorial(num-1)
		num *= newNum
	return num
number = factorial(100)

digits = str(number)
sum = 0

for l in digits:
	sum += int(l)

print sum	
