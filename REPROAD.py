tc = int(input(''))
while(tc>0):
    n,k = map(int,input('').split())
    road = input('').split()
    back=0
    front=0
    maxlen=0
    zeros=0
    while(back<n):
        if road[back]=='0':
            zeros+=1
        if zeros<=k:
            maxlen=max(back-front+1,maxlen)
        else:
            while(zeros>k ):
                if road[front]=='0':
                    zeros-=1
                front+=1
        back+=1
    print(maxlen)
    tc-=1
