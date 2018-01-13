def pythagorean():
	for a in range(2,900):
		for b in range(2, 900):
			c = 1000 - a - b
			if a**2 + b**2 == c**2:
				print 'Product: ' + str(a * b * c)
				print 'Factors: a : ' + str(a) + ', b : ' + str(b) + ', c : ' + str(c)
				return
pythagorean()
