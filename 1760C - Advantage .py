t = int(input())
for i in range(t):
    n = int(input())
    a=list(map(int,input().split()))
    b=sorted(a)
    m1=b[-1]
    m2=b[-2]
    li=[]
    for i in a:
        if i==m1:
            li.append(i-m2)
        else:
            li.append(i-m1)
    print(*li)
