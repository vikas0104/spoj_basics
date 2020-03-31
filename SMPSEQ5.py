n1 = int(input(""))
s1 = input("").split()
n2 = int(input(""))
s2 = input("").split()

for i in range(n1):
    #print(s1[i])
    if s1[i] == s2[i]:
        print(i+1,end=' ')
