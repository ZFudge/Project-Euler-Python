import math
def isPrime(num):
	for n in range(2,int(math.ceil(num))):
		if num % n == 0: return False
	else: return True
def checkNum(num):
	bigPrime = 0
	for n in range(2,int(math.ceil(num**0.5))):
		if num % n == 0 and isPrime(n): bigPrime = n
	print bigPrime	
num = 600851475143
checkNum(num)
