letters = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}

def letterVal(l):
        return letters[l]

def nameVal(name):
        nm = name.lower()
        value = 0
        for n in nm:
                if n != '"' and n != '\n': value += letterVal(n)
        return value

def indexMultiplier(value,index):
        return value * index

f = open('names.txt', 'r')
fr = f.read()
nameArray = fr.split(',')
f.close()

totalValue = 0

for indx,name in enumerate(nameArray):
        val = nameVal(name)
        val *= (indx + 1)
        totalValue += val

print totalValue

