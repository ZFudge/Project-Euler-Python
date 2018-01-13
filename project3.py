#A palindromic number reads the same both ways.
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
#Find the largest palindrome made from the product of two 3-digit numbers.
def isPalin(num):
        return str(num) == str(num)[::-1]
def findLargestPalinProd():
        largest = 0
        res = []
        for x in range(999,100,-1):
                for y in range(999,100,-1):
                        z = x*y
                        if isPalin(z) and largest < z:
                                largest = z
                                res = [x,y]
        print 'Largest product: ' + str(largest)
        print 'Two factors: ' + str(res[0]) + ' ' + str(res[1])
findLargestPalinProd()
