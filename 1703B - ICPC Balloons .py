    t = int(input())
    for i in range(t):
        n = int(input())
        s = input()
        seen = set()
        count=0
        for ch in s:
            if ch not in seen:
                count+= 2
                seen.add(ch)
            else:
                count+= 1
        print(count)
