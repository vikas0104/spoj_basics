test_case = int(input(""))
l = list()
for i in range(test_case):
    l.append(input(""))
for i in l:
    x,y = i.split()
    for j in range(int(x)):
        for k in range(int(y)):
            if j==0 or j==int(x)-1:
                print("*",end='')
            else:
                if k==0 or k==int(y)-1:
                    print("*",end="")
                else:
                    print(".",end="")
        print("")
    print("")
