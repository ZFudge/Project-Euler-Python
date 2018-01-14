x = 1
y = 1
fibCount = 2

def fib():
	global x,y,fibCount
	fibCount+=1
	z = x + y
	x = y
	y = z

while len(str(y)) < 1000:
	fib()

print "The index of the first number in the fibonacci sequence to have 1000 or more digits is {0}.".format(fibCount)
print "The number itself is {0}".format(y)
