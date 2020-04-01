#runtime NZEC error

tc = int(input(''))
nc=[]
coord=[]
s=[]
for i in range(tc):
    nc.append(int(input('')))
    for j in range(nc[i]):
        coord.append(input(''))
        x,y = coord[j].split()
        x = int(x)
        y = int(y)
        #print(x,y)
        s.append(abs(x+y))
    #print(s)
    print('Case '+str(i+1)+':',s.index(max(s))+1)
    #print('clearing')
    s.clear()
    #print(s)
    coord.clear()
#print(nc)
#print(coord)
