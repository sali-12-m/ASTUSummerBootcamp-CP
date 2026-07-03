t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    l=0
    r=n-1
    ans=0
    while True:
        while l<n and a[l]==0:
            l+=1
        while r>=0 and a[r]==1:
            r-=1
        if l>=r:
            break
        ans+=1
        l+=1
        r-=1
    print(ans)
