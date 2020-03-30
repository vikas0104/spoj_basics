test_case = int(input(""))
l = list()
for i in range(test_case):
    l.append(input(""))
for i in l:
    x,y = i.split()
    for j in range(3*int(x)+1):
        for k in range(3*int(y)+1):
            if j%3==0:
                print("*",end='')
            else:
                if k%3==0:
                    print("*",end='')
                else:
                    print(".",end='')
        print("")
    print("")
            
            
