tc = int(input(''))
l=[]
for i in range(tc):
    l.append(input(''))
def convert(a,b):
    if a.isdigit():
        a = int(a)
    else:
        a = float(a)
    if b.isdigit():
        b=int(b)
    else:
        b=float(b)
    return a,b
    
for pair in l:
    x,y = pair.split()
    x,y = convert(x,y)
    print(x+y)
