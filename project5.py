sum = 0
square = 0
for n in range(1,100):
	sum += n*n
	square += n
square *= square
print square - sum
