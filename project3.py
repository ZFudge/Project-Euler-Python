def isPalin(num):
	return str(num) == str(num)[::-1]

def findLargestPalinProd():
	largest = 0
	for x in range(999,100,-1):
		for y in range(999,100,-1):
			z = x*y
			if isPalin(z) and largest < z:
				largest = z
	print largest
findLargestPalinProd()
