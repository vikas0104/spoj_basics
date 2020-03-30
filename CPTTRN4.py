test_case = int(input(""))
l = list()
for i in range(test_case):
    l.append(input(""))
for i in l:
    x,y,a,b = i.split()
    for j in range(int(x)*int(a)+int(x)+1):
        for k in range(int(y)*int(b)+int(y)+1):
            if j%(int(a)+1)==0:
                print("*",end='')
            else:
                if k%(int(b)+1)==0:
                    print("*",end='')
                else:
                    print(".",end='')
        print("")
    print("")
            
            
