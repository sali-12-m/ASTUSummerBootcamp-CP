t = int(input())
for j in range(t):
    n = int(input())
    a=list(map(int,input().split()))
    l=0
    r=n-1
    count=1
    found=True
    while l<r:
        if a[l]==count:
            l+=1
        elif a[r]==count:
            r-=1
        else:
            found=False
            break
        count+=1
    if found:
        print("YES")
    else:
        print("NO")
