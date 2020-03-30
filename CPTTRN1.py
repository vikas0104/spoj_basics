test_case = int(input(""))
l = list()
for i in range(test_case):
    l.append(input(""))

for i in l:
    x,y = i.split()
    for i in range(int(x)):
        for j in range(int(y)):
            if i%2==0:
                if j%2==0:
                    print('*',end='')
                else:
                    print('.',end='')
            else:
                if j%2!=0:
                    print('*',end='')
                else:
                    print('.',end='')
        print("")
    print("")
