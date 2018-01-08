total = 0
def fib(n1,n2):
	global total
	if n2 % 2 == 0: total += n2;
	if n1 < 4000000 and n2 < 4000000: fib(n2, n1 + n2)
fib(1,2)
print total
