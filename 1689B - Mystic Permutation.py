t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    if n == 1:
        print(-1)
        continue

    q = list(range(1, n + 1))

    for i in range(n - 1):
        if q[i] == p[i]:
            q[i], q[i + 1] = q[i + 1], q[i]

    if q[n - 1] == p[n - 1]:
        q[n - 1], q[n - 2] = q[n - 2], q[n - 1]

    print(*q)