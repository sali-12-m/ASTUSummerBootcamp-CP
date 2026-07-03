t = int(input())
for j in range(t):
    n = int(input())
    s = input()
    m= []
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            m.append(i)
    if not m:
        print("Yes")
    else:
        ok = True
        for i in range(1, len(m)):
            if m[i]!= m[i - 1] + 1:
                ok = False
                break
        if ok:
            print("Yes")
        else:
            print("No")
