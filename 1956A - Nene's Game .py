t = int(input())
for i in range(t):
    k,q = map(int,input().split())
    a = list(map(int,input().split()))
    nums = list(map(int,input().split()))
    for j in nums:
        print(min(j, a[0] - 1), end=" ")
    print()
