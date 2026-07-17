    t = int(input())
     
    for i in range(t):
        n = int(input())
     
        a = input().split()
        b = input().split()
        c = input().split()
     
        d = {}
     
        for word in a + b + c:
            if word in d:
                d[word] += 1
            else:
                d[word] = 1
        score1 = score2 = score3 = 0
        for word in a:
            if d[word] == 1:
                score1 += 3
            elif d[word] == 2:
                score1 += 1
        for word in b:
            if d[word] == 1:
                score2 += 3
            elif d[word] == 2:
                score2 += 1
        for word in c:
            if d[word] == 1:
                score3 += 3
            elif d[word] == 2:
                score3 += 1
        print(score1, score2, score3)
