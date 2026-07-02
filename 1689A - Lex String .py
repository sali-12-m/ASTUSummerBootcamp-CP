t=int(input())
for i in range(t):
    a,b,k=map(int, input().split())
    s1= sorted(input())
    s2= sorted(input())
    i=0
    j=0
    c1=0
    c2=0
    ans=""
    while i < a and j < b:
        if (s1[i] < s2[j] and c1< k) or c2 == k:
            ans += s1[i]
            i += 1
            c1 += 1
            c2 = 0
        else:
            ans += s2[j]
            j+=1
            c2+=1
            c1=0
    print(ans)
