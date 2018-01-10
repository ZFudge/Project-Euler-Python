import math
def isPrime(num):
	for n in range(2, int(math.ceil(num**0.5)+1)):
		if num % n == 0: return False
	else: return True
start = 1
primes = 1 #counts start at 3
while primes < 10001:
	start += 2
	if isPrime(start): primes += 1
else: print start
