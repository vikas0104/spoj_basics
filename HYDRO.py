tc = int(input(''))
while(tc>0):
    n = int(input(''))
    h = input('').split()
    for i in range(n):
        h[i]= int(h[i])
    p_l=0
    p_r=n-1
    max_l=h[p_l]
    max_r=h[p_r]
    water=0
    while(p_r>p_l):
        if(max_l<max_r):
            p_l+=1
            if(h[p_l]>max_l):
                max_l=h[p_l]
            else:
                water+=max_l-h[p_l]
        else:
            p_r-=1
            if(h[p_r]>max_r):
                max_r=h[p_r]
            else:
                water+=max_r-h[p_r]
    tc-=1
    print(water)
