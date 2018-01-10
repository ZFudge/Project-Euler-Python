#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10,001st prime number?
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
