t = int(input())
for j in range(t):
    n = int(input())
    a=sorted(list(map(int,input().split())))
    blue = a[0]
    red = 0

    for i in range(1, n):
        blue += a[i]
        red += a[n - i]

        if red > blue:
            print("YES")
            break
    else:
        print("NO")
