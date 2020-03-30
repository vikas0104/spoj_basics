# your code goes here
test_cases = int(input(""))
stuff = list()
for i in range(test_cases):
	stuff.append(input(""))
for i in stuff:
    #print(len(i)/2)
    for j in range(int(len(i)/2)):
        if 2*j>= int(len(i)/2):
            break
        print(i[2*j],end = '')
    print("")
