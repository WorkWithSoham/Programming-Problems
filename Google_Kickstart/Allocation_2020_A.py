tc = int(input())
for t in range(tc):
    n, budget = map(int, input().split())
    houses = sorted((list(map(int, input().split()))))
    count = 0
    _sum = 0
    for i in range(n):
        _sum += houses[i]
        if _sum <= budget:
            count += 1
        else:
            break
    print("Case #"+str(t+1)+":", count)
