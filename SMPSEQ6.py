x,y = map(int,input("").split())
s1 = input("").split()
s2 = input("").split()

for i in range(x):
    for j in range(-y,y+1):
        if i+j<0 or i+j>=len(s2):
            continue
        elif s1[i]==s2[i+j]:
            #print(s1[i],s2[i+j],sep=' ')
            print(i+1)
