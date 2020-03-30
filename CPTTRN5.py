test_case = int(input(""))
l = list()
for i in range(test_case):
    l.append(input(""))
for i in l:
    x,y,a = i.split()
    for j in range(int(x)*int(a)+int(x)+1):
        for k in range(int(y)*int(a)+int(y)+1):
            if j%(int(a)+1)==0:
                print("*",end='')
            elif k%(int(a)+1)==0:
                print("*",end='')
            elif(int(j)+int(k))%(2*int(a) +2)==0:
                print("/",end="")
            elif(int(j)-int(k))%(2*int(a)+2)==0:
                print("\\",end='')
            else:
                print(".",end='')
        print("")
    print("")
