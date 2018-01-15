def collatz(num,count=0):
        if num != 1:
                if num % 2 == 0: return collatz(num/2,count+1)
                else: return collatz(num*3+1,count+1)
        else: return count + 1

largestCollatz = [0,0]

for n in range(100,1000000):
        col = collatz(n)
        if col > largestCollatz[0]: [largestCollatz[0],largestCollatz[1]] = [col,n]

print """The largest collatz sequence made from a starting
number under one million is {0} steps long.
The starting number to produce this chain is {1}.""".format(largestCollatz[0],largestCollatz[1])
