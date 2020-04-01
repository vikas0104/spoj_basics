tc = int(input(''))
l = list()
s=list()
primes=[]
for i in range(tc):
    l.append(int(input('')))
def getprime(x):
    for a in range(2,10000):
        for b in range(2,a):
            if a%b==0:
                break
        else:
            primes.append(a)
        if len(primes)==x:
            return primes
y = max(l)
p = getprime(3*y)
#print(p)
def getseries(z):
    count=0
    s.clear()
    for i in range(1,z+1):
        #print(p[count],p[count+1],p[count+2])
        s.append((p[count]*p[count+1])+p[count+2])
        count=count+3
    return s
for m in l:
    for i in getseries(m):
        print(i,end=' ')
    print('')
