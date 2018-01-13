#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.
import math
def isPrime(num):
	for f in range(2,int(math.ceil(num**0.5)+1)):
		if num % f == 0: return False
	else:	return True
primeSum = 2 # only even prime is 2, removed even checks from loop to save resources
for n in range(3, 2000000, 2):
	if isPrime(n): primeSum += n
print primeSum
