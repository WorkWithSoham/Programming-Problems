for _ in range(int(input())):
    n = int(input())
    exps = sorted(list(map(int, input().split())))

    i = 1
    count = 0
    for exp in exps:
        if i == exp:
            count += 1
            i = 0
        i += 1

    print(count)

    

