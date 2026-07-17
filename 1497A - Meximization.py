    t=int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        a=sorted(a)
        li=[]
        l2=[]
        for i in range(1,n):
            if a[i]!=a[i-1]:
                li.append(a[i-1])
            else:
                l2.append(a[i-1])
        li.append(a[-1])
        result=li+l2
        print(*result)
