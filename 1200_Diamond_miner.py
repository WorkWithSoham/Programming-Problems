from math import sqrt
tc = int(input())

for _ in range(tc):
    x = []
    y = []
    n = int(input())
    for _ in range(2*n):
        a, b = map(int, input().split())
        if a == 0:
            y.append(abs(b))
        else:
            x.append(abs(a))

    y = sorted(y)
    x = sorted(x)
    total = 0
    for i in range(len(x)):
        total += sqrt(x[i]**2 + y[i]**2)

    print(total)
